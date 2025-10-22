from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

with HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"🚀 Server running at http://localhost:{PORT}")
    httpd.serve_forever()
