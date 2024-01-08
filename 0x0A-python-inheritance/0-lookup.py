#!/usr/bin/python3
"""This module defines a function called lookup.

It takes obj as input and returns a list of all
available attributes and methods.
"""


def lookup(obj):
    """This function returns a list attrs and methods of objs"""

    """" Parameter:
           obj: object to return attrs and methods list.
    """

    return dir(obj)
