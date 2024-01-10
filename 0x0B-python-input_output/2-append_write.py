#!/usr/bin/python3
"""This module is about appending to a text file"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to be appended.

    Returns:
        int: The number of characters added.
    """
    # Open the file in append mode ('a')
    # and use 'with' statement for automatic file closing
    with open(filename, mode='a', encoding='utf-8') as file:
        # Append the text to the file
        file.write(text)
        # Return the number of characters added
        return len(text)
