import requests
import sys

def fetch_response(url):
    """Fetches the response from the given URL, handling potential errors.

    Args:
        url (str): The URL to fetch the response from.

    Returns:
        None if an HTTP error occurs, otherwise the response text.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for status codes >= 400
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error code:", e.response.status_code)
        return None

if __name__ == "__main__":
    url = sys.argv[1]
    response_text = fetch_response(url)
    if response_text is not None:
        print(response_text)
