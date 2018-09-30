import urllib2
import httplib
import server_client_utils as utils
import random
import ssl


def connect(url, code=None):
    """Does a single connection to @param url,
       if @param code is availible, also sends X-Return-Code header."""
    try:
        request = urllib2.Request(url)
        if code is not None:
            request.add_header('X-Return-Code', code)

        context = ssl.create_default_context(cafile="server.crt")
        context.check_hostname = True

        response = urllib2.urlopen(request, context=context)

        print("HTTP Response Code {}".format(response.code))
        html = response.read()
        print(html)
    except urllib2.HTTPError as err:
        print(err)
    except httplib.BadStatusLine as err:
        print("Bad status code")
    except urllib2.URLError as err:
        print(err)
    except ssl.CertificateError as err:
        print(err)
    except Exception:
        utils.error("Failed, terminating")


def main():
    random.seed()

    AMOUNT_OF_CONNECTS = 10
    # should be from 0, to 100, is probability in percents,
    # that an X-Code request would be sent
    PARTS_WITH_XCODE = 25

    TEST_URL_LIST = ["https://127.0.0.1:4443",
                     "https://127.0.0.1:4443/test_dir",
                     "https://127.0.0.1:4443/test_dir/text.txt",
                     "https://127.0.0.1:4443/fake_dir",
                     "https://127.0.0.1:4443/fake_file.faker"]

    TEST_CODES_LIST = [403, 102, 205, 206, 418]

    for i in range(0, AMOUNT_OF_CONNECTS):
        code = None
        if (random.randint(0, 101) < PARTS_WITH_XCODE):
            code = random.choice(TEST_CODES_LIST)
        connect(random.choice(TEST_URL_LIST), code)

    raw_input("Press anything to exit")


if __name__ == '__main__':
    main()
