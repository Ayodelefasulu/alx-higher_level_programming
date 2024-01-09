#!/usr/bin/python3
"""Module defining the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if object is instance of class
    that inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class.

    Returns:
        True if obj isinstanceof/inherited 4rm specified class, else False.
    """
    return isinstance(obj, a_class)
