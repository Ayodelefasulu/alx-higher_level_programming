#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


def search_user(letter):
    """Sends a POST request and parses a simple response format.

    Args:
        letter (str): The letter to search for.

    Returns:
        None if the response format is invalid or empty,
        otherwise a list containing user data ([id, name]).
    """

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise error for status_c >= 400

        # Check for empty response body
        if not response.text:
            return None

        # Split response by space (assuming format: [id] <name>)
        user_data = response.text.strip().split(" ")

        # Validate response format (two elements)
        if len(user_data) != 2:
            print("Not a valid JSON")
            return None

        # Try converting elements to integers and string
        try:
            user_id = int(user_data[0][1:-1])  # Remove brackets from id
            user_name = user_data[1]
        except ValueError:
            print("Not a valid JSON")
            return None

        return [user_id, user_name]
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
