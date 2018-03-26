import time
import BaseHTTPServer


HOST_NAME = 'localhost'
PORT_NUMBER = 8000


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(s):

        s.send_response(200)
        s.send_header('Content-Type', 'text/html')
        s.end_headers()

    def do_GET(s):

        fp = open(s.path)
        buf = ''
        for i in fp.readline():
            buf += i
        len_buf = len(buf)

        s.protocal_version = 'HTTP/1.1'

        s.send_response(200)

        s.send_header('Welcome', 'Content')
        s.send_header('Content-Length', len_buf)
        s.end_headers()

        s.wfile.write(buf)

    def do_POST(s):

        path = s.path
        datas = s.rfile.read(int(s.headers['content-length']))

        buf = '''
        <!DOCTYPE HTML>
        <html>
            <head><title>Post page</title></head>
            <body>Post Data:%s  <br />Path:%s</body>
        </html>''' % (datas, s.path)

        len_buf = len(buf)
        s.send_response(200)
        s.send_header('test', 'this is a test')
        s.send_header('Content-Length', len_buf)
        s.end_headers()

        s.wfile.write(buf)
        print buf


if __name__ == '__main__':

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), 'Server Starts -%s:%s' % (HOST_NAME, PORT_NUMBER)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER)
