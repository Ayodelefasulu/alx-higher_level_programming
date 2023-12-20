#!/usr/bin/python3

"""Module: 3-square

This module defines a class, Square, representing a
square with a private size attribute.

Classes:
    Square: A class for creating square objects with a private size attribute.

Attributes:
    __size (int): Private instance attribute representing size of the square.

Methods:
    __init__(self, size=0): Initializes a Square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

    area(self): Returns the current square area.

        Args:
            None.

        Returns:
            int: Square of the area.

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

    area_result = my_square.area()
    print(area_result)
"""


class Square:
    """Class representing a square with a private size attribute.

    Attributes:
        __size (int): Private instance attribute representing
        the size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square with an optional size.
        area(self): Return the current square area
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

    def area(self):
        """Returns the current square area.

        Args:
            None.

        Return:
            int: Square of the area.
        """

        return self.__size * self.__size
