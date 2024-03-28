#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response body.

This script takes a URL and an email as input, sends a POST request to the URL
with the email as a parameter, and displays the body of the response decoded in
utf-8. It uses the urllib.request module for handling the request and response.
"""

import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """Sends a POST request with the email and returns the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to send as a parameter.

    Returns:
        str: The body of the response, decoded in utf-8.
    """

    data = urllib.parse.urlencode({"email": email})  # Encode email as a parameter
    data = data.encode("utf-8")  # Encode data as bytes

    with urllib.request.urlopen(url, data=data) as response:
        return response.read().decode("utf-8")  # Decode response body


if __name__ == "__main__":
    url = sys.argv[1]  # Access the first command-line argument (the URL)
    email = sys.argv[2]  # Access the second command-line argument (the email)
    response_body = send_post_request(url, email)
    print(response_body)

