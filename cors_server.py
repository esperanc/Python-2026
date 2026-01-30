#!/usr/bin/env python3
"""
Servidor HTTP simples com CORS habilitado. Permite que arquivos
locais sejam acessados por scripts em outras origens.
Uso: python3 cors_server.py [porta]
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow requests from any origin
        self.send_header('Access-Control-Allow-Origin', '*')
        # Allow common methods
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        # Required for Private Network Access (CORS-RFC1918)
        # This allows public websites to access localhost
        self.send_header('Access-Control-Allow-Private-Network', 'true')
        # Allow headers that might be requested
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()
    
    def do_OPTIONS(self):
        # Handle preflight requests
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    # usage: python cors_server.py [port]
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f"Serving HTTP on port {port} with CORS enabled...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
