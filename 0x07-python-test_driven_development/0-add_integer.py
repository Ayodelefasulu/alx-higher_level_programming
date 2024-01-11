#!/usr/bin/python3
"""Adds two numbers and returns their integer sum.
    Example:
    0-add_integer(2, 10)
    12
"""


def add_integer(a, b=98):
    """Adds the two integers
    Raises:
        TypeError: if a and b is not integer or float"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
