#!/usr/bin/python3
"""Module: 6-square

This module defines the Square class,
representing a square with size and position attributes.

Classes:
    Square: A class representing a square.

Attributes:
    None

Functions:
    None

Notes:
    The Square class includes methods for initializing
    the square with size and position,
    retrieving and setting the size and position attributes,
    calculating the area,
    and printing the square to stdout.

Example:
    square_1 = Square(3)
    square_1.my_print()
    # Output:
    # ###
    # ###
    # ###

    square_2 = Square(3, (1, 1))
    square_2.my_print()
    # Output:
    #
    # ###
    # ###

    square_3 = Square(3, (3, 0))
    square_3.my_print()
    # Output:
    #
    #
    #
    # ###
    # ###
    # ###

    See module docstring for additional information.

"""

# ... [Class implementation]



class Square:
    """Class representing a square with size and position attributes.

    Attributes:
        __size (int): Private instance attribute
        representing the size of the square.
        __position (tuple): Private instance attribute
        representing the position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a Square.
        size(self): Getter method for retrieving the size attribute.
        size(self, value): Setter method for setting the size attribute.
        position(self): Getter method for retrieving the position attribute.
        position(self, value): Setter method for setting the position attribute.
        area(self): Public instance method returns current square area.
        my_print(self): Public instance method prints the square.

    Note:
        The size attribute must be an integer, and if less than 0,
        a ValueError is raised.
        The position attribute must be a tuple of 2 positive integers,
        and if not, a TypeError is raised.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates a Square with optional size and position.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square
                (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for retrieving the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for retrieving the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for setting the position attribute.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2\
            or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method prints the square with the character '#' to stdout."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

