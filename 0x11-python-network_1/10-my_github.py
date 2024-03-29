#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) and
uses the GitHub API to display the user ID.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <access_token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    # Set the GitHub API endpoint to fetch user information
    url = f"https://api.github.com/users/{username}"

    # Set the headers for Basic Authentication using the access token
    headers = {'Authorization': f'token {access_token}'}

    # Send a GET request to the GitHub API
    response = requests.get(url, headers=headers)

    # Check if the request was successful and parse the JSON response
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print("None")
