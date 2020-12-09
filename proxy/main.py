import argparse
from proxy.prox import ProxyRequestHandler, ThreadingHTTPServer


def start():
    handlerClass = ProxyRequestHandler
    serverClass = ThreadingHTTPServer
    protocol = "HTTP/1.1"
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='port', default=8080)
    parser.add_argument('--address', help='address', default='::1')
    args = parser.parse_args()
    server_address = (args.address, int(args.port))

    handlerClass.protocol_version = protocol
    httpd = serverClass(server_address, handlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTP Proxy on {} port {} ...".format(sa[0], sa[1]))
    httpd.serve_forever()


if __name__ == '__main__':
    start()