import urllib2, httplib
import server_client_utils as utils

def main():
    
    try:
        request = urllib2.Request("http://127.0.0.1:8080")
        #request.add_header('X-Return-Code', 101)

        response = urllib2.urlopen(request)
    
        print("HTTP Response Code {}".format(response.code))
        html = response.read()
        print(html)
    except urllib2.HTTPError as err:
        print(err)
    except httplib.BadStatusLine as err:
        print("Bad status code")
    except:
        utils.error("Unknown error, terminating")

if __name__ == '__main__':
    main()