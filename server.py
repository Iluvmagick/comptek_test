import BaseHTTPServer, SimpleHTTPServer
import sys
import server_client_utils as utils

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = "/www" + self.path
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def run_server(address):
    """Launches BaseHTTPServer on the address specified by function parameter."""
    try:
        httpd = BaseHTTPServer.HTTPServer(address, RequestHandler)
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