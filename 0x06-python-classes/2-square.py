#!/usr/bin/python3

"""Module: 2-square

This module defines a class, Square, representing a
square with a private size attribute.

Classes:
    Square: A class for creating square objects with
    a private size attribute.

Attributes:
    None.

Methods:
    __init__(self, size=0): Initializes a Square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

Example:
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    my_square_default = Square()
    print(type(my_square_default))
    print(my_square_default.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)

    try:
        my_square_invalid = Square("3")
        print(type(my_square_invalid))
        print(my_square_invalid.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_negative = Square(-89)
        print(type(my_square_negative))
        print(my_square_negative.__dict__)
    except Exception as e:
        print(e)
"""


class Square:
    """Class representing a square with a private size attribute.

    Attributes:
        __size (int): Private instance attribute representing
        the size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square with an optional size.
    """

    def __init__(self, size=0):
        """Instantiates a Square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
