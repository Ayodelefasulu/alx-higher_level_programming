#!/usr/bin/python3
"""Fetches the X-Request-Id header value from a URL.

This script takes a URL as input, sends a request to the URL, and extracts
the value of the X-Request-Id header from the response. It uses a with
statement to ensure proper resource management.
"""

import urllib.request
import sys


def get_request_id(url):
    """Fetches the X-Request-Id value from the given URL.

    Args:
        url (str): The URL to fetch the X-Request-Id from.

    Returns:
        str: The value of the X-Request-Id header, or an empty string if not found.
    """

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        return headers.get("X-Request-Id", "")


if __name__ == "__main__":
    url = sys.argv[1]  # Access the first command-line argument (the URL)
    request_id = get_request_id(url)
    print(request_id)
