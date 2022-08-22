from http.server import BaseHTTPRequestHandler
import json
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        ip=self.client_address[0]
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data={'code':200,'msg':'成功','ip':ip}
        res=json.dumps(data)
        self.wfile.write(res.encode())
        return