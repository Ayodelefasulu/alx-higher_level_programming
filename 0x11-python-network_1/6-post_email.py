#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request to the
passed URL with the email as parameter, and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    # Send a POST request with the email as a parameter
    response = requests.post(url, data={'email': email})

    # Display the body of the response
    print(response.text)
