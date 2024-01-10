#!/usr/bin/python3
"""This module creates an object from a json file"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON file.

    Example:
        filename = "my_list.json"
        my_list = load_from_json_file(filename)
        print(my_list)
        print(type(my_list))
    """
    with open(filename, 'r') as file:
        return json.load(file)
