#!/usr/bin/python3
"""A script that sends request to
https://intranet.hbtn.io/status and print the body of the response.
"""


if __name__ == '__main__':
    import requests
    request = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t type: {}".format(type(request.text)))
    print("\t content: {}".format(request.text))
