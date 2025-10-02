import os
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler, HTTPServer
load_dotenv()  # Carica le variabili dal file .env

debug = os.getenv("DEBUG")

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if(debug):
          self.wfile.write(bytes("<html><body><h1> DEBUG-Hello from Python!</h1></body></html>", "utf-8"))
        else:
          self.wfile.write(bytes("<html><body><h1>Hello from Python!</h1></body></html>", "utf-8"))

if __name__ == "__main__":
    server_address = ("144.91.83.75", 8080)
    httpd = HTTPServer(server_address, MyServer)
    print("Server avviato su http://localhost:8080")
    httpd.serve_forever()
