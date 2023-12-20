#!/usr/bin/python3

"""Module: 4-square

This module defines a class, Square,
representing a square with a private size attribute.

Classes:
    Square: A class for creating square objects with a private size attribute.

Attributes:
    __size (int): Private instance attribute
    representing the size of the square.

Methods:
    __init__(self, size=0): Initializes a Square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

    area(self): Returns the current square area.

        Returns:
            int: Square of the area.

    size(self): Getter method to retrieve the value of the size attribute.

        Returns:
            int: The size of the square.

    size(self, value): Setter method to set the value of the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

Example:
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
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
        area(self): Return the current square area
        size(self): Returns size of square area
        size(self, value): Sets size of square area
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

    @property
    def size(self):
        """Returns size of square area.

        Args:
            None.

        Return:
            int: Square of the area.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square area.

        Args:
            int: Value to be set.

        Raises:
           TypeError: If size is not an integer.
           ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
