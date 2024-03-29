#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL using urllib, and
displays the value of the X-Request-Id variable found in the header of the
response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Send a GET request to the specified URL using urllib
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response")
