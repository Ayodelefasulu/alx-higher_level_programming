#!/usr/bin/python3
"""
This script fetches the status of the URL "https://alx-intranet.hbtn.io/status"
and displays the body of the response in a specific format.
"""

import requests

if __name__ == "__main__":
    # Define the URL to fetch
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    response = requests.get(url)

    # Display the body of the response in a formatted manner
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
