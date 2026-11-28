"""Serve a directory (docs/ by default) locally, telling the browser not to
cache anything so a rebuilt font shows on a plain reload (the font files keep
the same names). `make lab` serves the repo root on its own port, for lab/ to
load fonts/.

With --rebuild (`make lab`), a background loop watches the .py sources: when
one changes, the OTF fonts are rebuilt, then /events tells the open pages,
which load the new fonts in place. A request under /fonts/otf/ waits for a
build in progress. A failed build answers 500 with its traceback.
"""

import functools
import http.server
import logging
import os
import pathlib
import subprocess
import sys
import threading
import time

import nordwand_mono

ROOT = pathlib.Path(__file__).resolve().parents[3]
SOURCES = pathlib.Path(nordwand_mono.__file__).parent
STAMP = ROOT / "fonts" / "otf" / "NordwandMono-Regular.otf"
LOCK = threading.Lock()
# (source mtime, stderr) of the last failed build, not retried until a source
# changes again
FAILED = None
# Successful builds, and the count last announced on /events
BUILDS = 0
ANNOUNCED = 0
REBUILT = threading.Condition()
log = logging.getLogger("serve")


def newest_source():
    """The most recently changed source file."""
    return max(SOURCES.rglob("*.py"), key=lambda p: p.stat().st_mtime)


def ensure_built():
    """Build the OTF fonts if they are missing or older than a source; the
    build's stderr if it failed, else None."""
    global FAILED, BUILDS
    with LOCK:
        source = newest_source()
        mtime = source.stat().st_mtime
        if STAMP.exists() and STAMP.stat().st_mtime >= mtime:
            return None
        if FAILED and FAILED[0] == mtime:
            return FAILED[1]
        log.info("Rebuilding, %s changed", os.path.relpath(source, ROOT))
        start, began = time.monotonic(), time.time()
        run = subprocess.run(
            [sys.executable, "-m", "nordwand_mono.generate_font", "-j", "--otf"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if run.returncode:
            log.error("Build failed after %.1fs\n%s", time.monotonic() - start, run.stderr)
            FAILED = (mtime, run.stderr)
            return run.stderr
        FAILED = None
        BUILDS += 1
        # Dated from the build's start: a save during the build rebuilds again
        os.utime(STAMP, (began, began))
        log.info("Rebuilt in %.1fs", time.monotonic() - start)
        return None


def watch(interval=0.3):
    """Rebuild whenever a source changes, and announce it on /events."""
    # ponytail: polls mtimes (a few ms), watchdog if it gets slow
    global ANNOUNCED
    while True:
        ensure_built()
        if BUILDS != ANNOUNCED:
            with REBUILT:
                ANNOUNCED = BUILDS
                REBUILT.notify_all()
        time.sleep(interval)


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


class RebuildHandler(NoCacheHandler):
    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/events":
            return self.events()
        error = path.startswith("/fonts/otf/") and ensure_built()
        if error:
            self.send_error(500, "Build failed", error)
            return
        super().do_GET()

    def events(self):
        """Server-sent events: `rebuilt` after each rebuild, for the pages to
        load the new fonts; a comment every 15s keeps the stream open."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        seen = ANNOUNCED
        try:
            while True:
                with REBUILT:
                    REBUILT.wait_for(lambda: ANNOUNCED != seen, timeout=15)
                if ANNOUNCED != seen:
                    seen = ANNOUNCED
                    self.wfile.write(b"data: rebuilt\n\n")
                else:
                    self.wfile.write(b": ping\n\n")
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
    rebuild = "--rebuild" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--rebuild"]
    directory = args[0] if args else "docs"
    port = int(args[1]) if len(args) > 1 else 8000
    handler = functools.partial(RebuildHandler if rebuild else NoCacheHandler, directory=directory)
    if rebuild:
        threading.Thread(target=watch, daemon=True).start()
    print(f"Serving {directory} on http://localhost:{port}/")
    # Local only: the lab serves the whole repo
    http.server.ThreadingHTTPServer(("localhost", port), handler).serve_forever()
