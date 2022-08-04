#!/usr/bin/python3
"""A scrip that takes the github repo name and
the owner name and prints the sha and author name"""


if __name__ == '__main__':

    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    result = response.json()
    for i in range(2):
        author = result[i]['commit']['author']['name']
        sha = result[i]['sha']
        print("{}: {}".format(sha, author))
