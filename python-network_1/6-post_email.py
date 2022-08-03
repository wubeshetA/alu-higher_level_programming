#!/usr/bin/python3
"""A script that sends POST requests and display the response."""


if __name__ == '__main__':
    import requests
    import sys

    payload = {'email': sys.argv[2]}
    request = requests.post(sys.argv[1], data=payload)
    print("{}".format(request.text))
