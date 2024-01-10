#!/usr/bin/python3
"""This is `from_json_string` module"""


import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string.

    Note:
        Uses the 'json.loads' function for deserialization.
    """
    return json.loads(my_str)
