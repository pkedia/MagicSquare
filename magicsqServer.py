import BaseHTTPServer
import urlparse
import json
from magic_square import *

port = 9000 # Maybe set this to 9000.
content_type = "text/html"

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    querysize = '<!DOCTYPE html>\n<html>\n <body>\n<form  method="GET">\n Size of Magic Square:\n <input type="text" name="size" value="3">\n<br>\n<input type="submit" value="Submit">\n</form>'
    def do_HEAD(self):
      self.send_response(200)
      self.send_header('Content-Type', content_type)
      self.end_headers()

    def do_GET(self):
      size=0
      """Respond to a GET request."""
      print(self.path)
      result =self.path.partition('size=')
      if len(result[2]) > 0:
        size = int(result[2])
      else:
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(self.querysize)
        
      if size > 0:
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(main(size))

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(("localhost", port), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()