#!/usr/bin/python3
"""This is an input/output module

Functions:
    read_file: That reads file line by line

Argument(s):
    filename: This is the name of the file

Returns: None
"""


def read_file(filename=""):
    """This function prints the lines of a file"""

    with open(filename, "r") as f:
        for l in f:
            print(l, end="")
