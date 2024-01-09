#!/usr/bin/python3
"""Module defining the is_same_class function."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class.

    Returns:
        True if object is exactly instance of specified class, else False.
    """
    return type(obj) is a_class
