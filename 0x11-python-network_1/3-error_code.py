#!/usr/bin/python3
"""Fetches the body of the response from a URL, handling HTTP errors.

This script takes a URL as input, sends a request to the URL, and manages
urllib.error.HTTPError exceptions, displaying their status codes. It prints
the body of the response decoded in utf-8 if the request is successful.
"""

import urllib.request
import sys


def fetch_response(url):
    """Fetches the response from the given URL, handling HTTP errors.

    Args:
        url (str): The URL to fetch the response from.

    Returns:
        None if an HTTPError occurs, otherwise the decoded response body.
    """

    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
        return None


if __name__ == "__main__":
    url = sys.argv[1]
    response_body = fetch_response(url)
    if response_body is not None:
        print(response_body)
