import BaseHTTPServer
import sys

def error(info, exit = True, code = -1):
    """Base fatal error handling, prints info, exit if @param exit, returning @param code"""
    print(info)
    if exit:
        sys.exit(code)

def address_handling():
    """Does read the address from command line arguments, returns it, defaults to DEFAULT_ADRESS, defined inside."""

    DEFAULT_ADRESS = "0.0.0.0:8080"

    try:
        address = sys.argv[1]
    except:
        address = DEFAULT_ADRESS

    try:
        address = tuple(address.split(':'))
        address = (address[0], int(address[1]))
    except:
        error("Can't parse address")
    finally:
        print("Launching server on address {}:{}".format(address[0], address[1]))

    return address

def run_server(address):
    """Launches BaseHTTPServer on the address specified by function parameter."""
    try:
        httpd = BaseHTTPServer.HTTPServer(address, BaseHTTPServer.BaseHTTPRequestHandler)
    except:
        error("Failed to launch server")
    
    print("Server launched!")

    # request handling loop until something goes wrong
    while(True): 
        try:
            httpd.handle_request()
        except:
            print("Server finished running, closing...")
            exit(0)

def main():
    address = address_handling()
    run_server(address)

if __name__ == '__main__':
    main()