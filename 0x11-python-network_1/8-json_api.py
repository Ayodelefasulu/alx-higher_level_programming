#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys
import json


def search_user(letter):
    """Sends a POST request and parses the JSON response.

    Args:
        letter (str): The letter to search for.

    Returns:
        None if the response is invalid JSON or empty,
        otherwise a list containing user data ([id, name]).
    """

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise error for status codes >= 400

        # Check for empty response body
        if not response.text:
            return None

        # Try parsing JSON
        user_data = json.loads(response.text)
        if not isinstance(user_data, list) or len(user_data) != 2:
            print("Not a valid JSON")
            return None

        return user_data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    user_data = search_user(letter)

    if user_data:
        print(f"[{user_data[0]}], {user_data[1]}")
    else:
        print("No result")
