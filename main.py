from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_GET(self):

        #Si on va sur la page de base
        if self.path == "/":
            self.path = '/index.html'


        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)

        #
        #
        #

        #Si on va Nul part
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8080), Server)
    print('Server is running')
    httpd.serve_forever()
    print('Server Stopped!')
