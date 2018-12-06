# -*- coding:utf-8 -*-
import http.server
import socketserver
def work():
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    work()
