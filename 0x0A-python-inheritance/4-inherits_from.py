#!/usr/bin/python3
"""Module defining the inherits_from function."""


def inherits_from(obj, a_class):
    """
    Check if obj isinstanceof class that inherited (directly/indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class.

    Returns:
        True if obj isinstanceof class that inherited from specified class,
        else False.
    """
    return issubclass(type(obj), a_class)
