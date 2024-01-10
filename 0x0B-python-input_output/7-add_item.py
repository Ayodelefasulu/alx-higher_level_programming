#!/usr/bin/python3
"""
Script: 7-add_item.py

This script adds command line arguments to a Python list...
...and saves them to a file named 'add_item.json'.
It utilizes the save_to_json_file and load_from_json_file...
...functions for handling JSON data.

Usage:
    $ ./7-add_item.py [arguments]

Args:
    arguments (list): List of strings to be added to existing list.

Notes:
    - List is saved as JSON representation in file -> 'add_item.json'.
    - If the file doesn’t exist, it is created.
    - File permissions and exceptions are not managed.

Examples:
    $ ./7-add_item.py Best School
        Adds "Best" and "School" to the list in 'add_item.json'.

    $ ./7-add_item.py 89 Python C
        Adds "89", "Python", and "C" to the list in 'add_item.json'.
"""


import sys
from os.path import isfile
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_items_to_list_and_save(arguments):
    """
    Adds provided arguments to existing list&saves to 'add_item.json'.

    Args:
        arguments (list): List of strings to be added to existing list.

    Returns:
        None
    """

    # Check if the file exists, if not, create it
    if not isfile('add_item.json'):
        save_to_json_file([], 'add_item.json')

    # Load the existing list from the file
    existing_list = load_from_json_file('add_item.json')

    # Add the new arguments to the existing list
    existing_list.extend(arguments)

    # Save the updated list back to the file
    save_to_json_file(existing_list, 'add_item.json')
