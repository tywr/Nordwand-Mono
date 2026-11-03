"""Serve a directory (docs/ by default) locally, telling the browser not to
cache anything so a rebuilt font shows on a plain reload (the font files keep
the same names). `make lab` serves the repo root on its own port, for lab/ to
load fonts/."""

import functools
import http.server
import sys


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "docs"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    handler = functools.partial(NoCacheHandler, directory=directory)
    print(f"Serving {directory} on http://localhost:{port}/")
    # Local only: the lab serves the whole repo
    http.server.ThreadingHTTPServer(("localhost", port), handler).serve_forever()
