from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

handler = SimpleHTTPRequestHandler

with HTTPServer(("", PORT), handler) as server:
    print(f"Servidor rodando na porta {PORT}")
    server.serve_forever()
