from http.server import BaseHTTPRequestHandler
import json
data={
    'code':200,
    'msg':'成功',
    'ip':'',
}
res=json.dumps(data,ensure_ascii=False,indent=4)
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(res.encode())
        return