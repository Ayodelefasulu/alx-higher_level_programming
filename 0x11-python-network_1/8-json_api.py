#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    # Send a POST request with the letter as a parameter
    response = requests.post(url, data=data)

    try:
        # Try to parse the response as JSON
        json_data = response.json()

        # Check if JSON is empty
        if not json_data:
            print("No result")
        else:
            # Display the id and name from the JSON data
            print(f"[{json_data['id']}] {json_data['name']}")
    except ValueError:
        # Handle invalid JSON format
        print("Not a valid JSON")
