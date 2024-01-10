#!/usr/bin/python3
"""This module returns serialized properties of class to json file
"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    (list, dictionary, string, integer, and boolean)...
    ...for JSON serialization of an object.

    Args:
        obj (object): An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representing JSON-serializable structure of object.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Iterate through the attributes and create a dictionary
    json_dict = {}
    for key, value in attributes.items():
        # Check if the attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
