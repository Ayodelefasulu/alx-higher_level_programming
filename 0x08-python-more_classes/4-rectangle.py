#!/usr/bin/python3
"""Module: rectangle

This module defines the Rectangle class, representing a geometric rectangle.

Classes:
    Rectangle:
        A class that defines a rectangle by specifying its width and height. It
        provides properties and methods to access and modify these attributes,
        ensuring they adhere to specific constraints.

Attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.

Methods:
    __init__(self, width=0, height=0):
        Initializes a new Rectangle instance with optional width and height.

    @property
    width(self):
        Retrieves the width of the rectangle.

    @width.setter
    width(self, value):
        Sets the width of the rectangle.
        Args:
            value (int): The width value to set.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.

    @property
    height(self):
        Retrieves the height of the rectangle.

    @height.setter
    height(self, value):
        Sets the height of the rectangle.
        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.

    area(self):
        Computes and returns the rectangle area.

    perimeter(self):
        Computes and returns the rectangle perimeter.
        If width or height is equal to 0, perimeter is equal to 0.

    __str__(self):
        Returns a string representation of the rectangle using '#' character.
        If width or height is equal to 0, returns an empty string.

    __repr__(self):
        Returns a string repr of rect obj to be able to recreate a new insta.

Example:
    Creating an instance of Rectangle:
    ```python
    my_rectangle = Rectangle(width=5, height=10)
    ```

Note:
    This module provides a basic implementation of the Rectangle class,
    allowing for the creation and manipulation of rectangle objects.

"""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rec instance with optional width and height.

        @property
        width(self):
            Retrieves the width of the rectangle.

        @width.setter
        width(self, value):
            Sets the width of the rectangle.
            Args:
                value (int): The width value to set.
            Raises:
                TypeError: If width is not an integer.
                ValueError: If width is less than 0.

        @property
        height(self):
            Retrieves the height of the rectangle.

        @height.setter
        height(self, value):
            Sets the height of the rectangle.
            Args:
                value (int): The height value to set.
            Raises:
                TypeError: If height is not an integer.
                ValueError: If height is less than 0.

        area(self):
            Computes and returns the rectangle area.

        perimeter(self):
            Computes and returns the rectangle perimeter.
            If width or height is equal to 0, perimeter is equal to 0.

        __str__(self):
            Returns a string representation of the rectangle using '#' char.
            If width or height is equal to 0, returns an empty string.

        __repr__(self):
            Returns a string repr of rect obj to recreate a new instance.

    Example:
        Creating an instance of Rectangle:
        ```python
        my_rectangle = Rectangle(width=5, height=10)
        ```

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes and returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Computes and returns the rectangle perimeter.

        If width or height is equal to 0, perimeter is equal to 0.
        """
        return 2 * (self.__width + self.__height)\
            if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """Returns a string representation of the rectangle using '#' char.

        If width or height is equal to 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'\
                .join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns string repr of rect obj to recreate new instance."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"
