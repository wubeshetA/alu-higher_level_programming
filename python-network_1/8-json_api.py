#!/usr/bin/python3
"""A script that sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


from requests import request


if __name__ == '__main__':
    import requests
    import sys

    letter = sys.argv[1]
    request = requests.post(
        'http://0.0.0.0:5000/search_user', params={'p': letter})
    try:
        request_dict = request.json()
        id = request_dict.get('id')
        name = request_dict.get('name')
        if len(request_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
