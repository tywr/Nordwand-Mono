"""Serve docs/ locally, telling the browser not to cache anything so a rebuilt
font shows on a plain reload (the font files keep the same names)."""

import functools
import http.server


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    handler = functools.partial(NoCacheHandler, directory="docs")
    print("Serving docs/ on http://localhost:8000")
    http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()
