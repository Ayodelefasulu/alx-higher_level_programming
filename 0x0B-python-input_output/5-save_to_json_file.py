#!/usr/bin/python3
"""This module saves object to json file"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file.

    Note:
        Uses the 'json.dump' function for serialization.

    Example:
        filename = "my_list.json"
        my_list = [1, 2, 3]
        save_to_json_file(my_list, filename)
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
