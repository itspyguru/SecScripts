from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class RequestLoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log request details
        self.custom_log_request()
        
        # Send a response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'GET request received and logged.')

    def do_POST(self):
        # Log request details
        self.custom_log_request()
        
        # Read and log the body of the POST request
        content_length = int(self.headers['Content-Length'])  # Get payload length
        post_data = self.rfile.read(content_length)  # Read the payload
        logging.info(f"POST Body: {post_data.decode('utf-8')}")

        # Send a response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'POST request received and logged.')

    def custom_log_request(self):
        logging.info(f"Request from {self.client_address[0]}:{self.client_address[1]}")
        logging.info(f"Method: {self.command}, Path: {self.path}")
        logging.info(f"Headers: {self.headers}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    server_address = ('', 8081)  # Listen on all interfaces, port 8081
    httpd = HTTPServer(server_address, RequestLoggerHandler)
    logging.info("Starting server on port 8081, use <Ctrl+C> to stop...")
    httpd.serve_forever()
