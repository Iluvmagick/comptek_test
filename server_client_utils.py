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
        print("Could not parse, or no address, launching with default server address {}".format(DEFAULT_ADRESS))
        address = DEFAULT_ADRESS

    try:
        address = tuple(address.split(':'))
        address = (address[0], int(address[1]))
    except:
        error("Can't parse address")
    finally:
        print("Launching server on address {}:{}".format(address[0], address[1]))

    return address