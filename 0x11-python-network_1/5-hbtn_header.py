#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the value
of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the script was given a URL argument
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]  # Get the URL from command-line argument

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code} - Failed to fetch data fr {url}")
        sys.exit(1)

    # Check if 'X-Request-Id' exists in the response headers
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)

    else:
        print("Error: 'X-Request-Id' not found in the response headers")
        sys.exit(1)
