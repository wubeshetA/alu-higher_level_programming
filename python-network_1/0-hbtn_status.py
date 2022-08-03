#!/usr/bin/python3
from urllib.request import urlopen
"""fetches data from using urllib.request"""

with urlopen("https://intranet.hbtn.io/status") as response:
    data = response.read()
    print("Body response:")
    print(f"    - type: {type(data)}")
    print(f"    - content: {data}")
    print(f"    - utf8 content: {data.decode('utf8')}")
