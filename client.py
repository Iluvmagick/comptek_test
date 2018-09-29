import urllib2
import server_client_utils as utils

def main():
    address = utils.address_handling()
    response = urllib2.urlopen("http://127.0.0.1:8080")
    html = response.read()
    print(html)

if __name__ == '__main__':
    main()