#!/usr/bin/python3
"""This module searches and inserts text"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text to file after each line containing specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str):
            The string to insert after each line containing the search string.
    """
    try:
        with open(filename, 'r+') as file:
            lines = file.readlines()
            file.seek(0)

            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

            file.truncate()

    except FileNotFoundError:
        pass  # File doesn't exist, no need to handle the exception
