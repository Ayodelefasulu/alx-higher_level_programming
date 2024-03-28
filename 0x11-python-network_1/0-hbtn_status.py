#!/usr/bin/python3
"""Fetches the status from a URL and displays the response body.

This script uses the urllib package to fetch the status from a URL and displays
the body of the response in a user-friendly format. It uses a with statement
to ensure proper resource management.
"""

import urllib.request


def fetch_status(url="https://alx-intranet.hbtn.io/status"):
    """Fetches the status from the given URL and displays the response body.

    Args:
        url (str, optional): The URL to fetch the status from. Defaults to
            "https://alx-intranet.hbtn.io/status".
    """

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()
