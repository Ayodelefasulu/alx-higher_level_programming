#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the body
of the response. If the HTTP status code is greater than or equal to 400, it
prints an error message.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Display the body of the response
    print(response.text)

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
