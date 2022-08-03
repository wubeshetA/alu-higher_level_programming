#!/usr/bin/python3
"""A script that sends a request and returns the body of the request.
"""


if __name__ == '__main__':
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
