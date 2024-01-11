#!/usr/bin/python3
"""This module contain a function that indents text"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    line = ""

    # Iterate through each character in the text
    for char in text:
        # Add the character to the current line
        line += char

        # Check if the character is '.', '?', or ':'
        if char in ['.', '?', ':']:
            # Print the current line without spaces at the beginning or end
            print(line.strip())

            # Reset the line for the next iteration
            line = ""

    # Print the last line if it's not empty
    if line:
        print(line.strip())
