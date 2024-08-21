from http.server import BaseHTTPRequestHandler, HTTPServer
from app.routes import get_properties
import json
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path == '/properties':
            query_params = parse_qs(parsed_url.query)
            filters = {
                'year': query_params.get('year', [None])[0],
                'city': query_params.get('city', [None])[0],
                'status': query_params.get('status', [None])[0],
            }

            # Imprimir parámetros en los logs de Docker
            print(f"Received parameters: {filters}")

            try:
                properties = get_properties(filters)
                print(f"Properties retrieved: {properties}")
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps([prop.to_dict() for prop in properties]).encode())
            except Exception as e:
                print(f"Error retrieving properties: {e}")
                self.send_response(500)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()