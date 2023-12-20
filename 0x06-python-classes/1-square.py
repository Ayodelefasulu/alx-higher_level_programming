#!/usr/bin/python3

"""Module: 1-square

This module defines a class, Square, representing a square with a private size attribute.

Classes:
    Square: A class for creating square objects with a private size attribute.

Attributes:
    None.

Methods:
    __init__(self, size): Instantiates a Square with a given size.

Notes:
    - The size attribute is private, and its name is modified using name mangling
      to include the class name, ensuring privacy and encapsulation.

Example:
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
"""


class Square:
    """This is a square class."""
    def __init__(self, size):
        """Instantiates a square with size ``size``.

        Args:
            size (int): The size of the square

        Note:
            The size attribute is private, and its modified to
            include the class name to make it private, name mangling.
        """
        self.__size = size
