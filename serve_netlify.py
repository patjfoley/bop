"""Local dev server that mimics the Netlify _redirects rules for this site.
Used only for previewing; not deployed."""
import http.server
import functools

REWRITES = {"/privacy": "/privacy.html", "/terms": "/terms.html", "/app": "/app.html"}


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0]
        if path.startswith("/b/") and not path.startswith("/b.html"):
            # Netlify: /b/*  /b.html  200  (URL preserved, content rewritten)
            self.path = "/b.html"
        elif path.startswith("/u/") and not path.startswith("/u.html"):
            self.path = "/u.html"
        elif path in REWRITES:
            self.path = REWRITES[path]
        return super().do_GET()


if __name__ == "__main__":
    http.server.ThreadingHTTPServer(("127.0.0.1", 8643), Handler).serve_forever()
