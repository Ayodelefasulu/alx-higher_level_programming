"""
Module: write_file

Provides function to write string to text file & return character count.
"""


def write_file(filename="", text=""):
    """
    Writes 'text' to 'filename' (UTF-8) and returns the character count.

    Args:
        filename (str): The file name.
        text (str): The string to be written.

    Returns:
        int: Number of characters written.

    Note:
        Creates the file if it doesn’t exist, overwrites if it does.
        Uses 'with' for automatic file closing no permission handling.

    Example:
        nb_characters =
            write_file("my_first_file.txt", "This School is so cool!\n")
        print(nb_characters)
    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
