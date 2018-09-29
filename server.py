import BaseHTTPServer, SimpleHTTPServer
import sys
import server_client_utils as utils
import ssl

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = "/www" + self.path 
        try:
            code = int(self.headers.getheader("X-Return-Code"))
            self.send_error(code, "X-Return-Code Matched!")
        except:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def run_server(address):
    """Launches BaseHTTPServer on the address specified by function parameter."""
    try:
        httpd = BaseHTTPServer.HTTPServer(address, RequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
    except:
        utils.error("Failed to launch server")
    
    print("Server launched!")

    # request handling loop until something goes wrong
    while(True): 
        try:
            httpd.handle_request()
        except:
            print("Server finished running, closing...")
            exit(0)

def main():
    address = utils.address_handling()
    run_server(address)

if __name__ == '__main__':
    main()