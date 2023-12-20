#!/usr/bin/python3

"""Module: 5-square

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

    my_print(self): Prints the square using the character '#'.

Example:
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
"""


class Square:
    """Class representing a square with a private size attribute.

    Attributes:
        __size (int): Private instance attribute
        representing the size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square with an optional size.
        area(self): Returns the current square area.
        size(self): Getter method to retrieve the value size attribute.
        size(self, value): Setter method to set the value size attribute.
        my_print(self): Prints out some gibberish

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """Instantiates a Square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the value of the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: Square of the area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints some gibberish

        Args:
            None.

        Returns:
            None.
        """
        if self.__size == 0:
            print(" ")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
