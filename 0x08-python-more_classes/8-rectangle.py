#!/usr/bin/python3
"""Module: 8-rectangle

Description:
    Defines a rectangle with width, height, and additional features.

Author:
    [Your Name]

Class:
    Rectangle:
        A class that defines a rectangle.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

Class Attributes:
    number_of_instances (int):
    A count of the number of instances of the Rectangle class.
    print_symbol (any):
    The symbol used for string representation. Initialized to '#'.

Methods:
    __init__(self, width=0, height=0):
        Initializes new Rectangle instance with optional width and height.

    area(self):
        Calculates and returns the area of the rectangle.

    perimeter(self):
        Calculates and returns the perimeter of the rectangle.
        If width or height is equal to 0, the perimeter is 0.

    __str__(self):
        Returns string representation of rectangle using the print_symbol.
        If width or height is equal to 0, returns an empty string.

    __repr__(self):
        Returns string repr of rect to recreate a new instance using eval().

    __del__(self):
        Prints a farewell message when an instance of Rectangle is deleted.

    @staticmethod
    bigger_or_equal(rect_1, rect_2):
        Returns the biggest rectangle based on the area.
        rect_1 must be an instance of Rectangle.
        rect_2 must be an instance of Rectangle.
        Returns rect_1 if both have the same area value.

Example:
    Example usage is provided at the end of the module.

Note:
    All instance and class attributes are private.
"""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int):
        A count of the number of instances of the Rectangle class.
        print_symbol (any): The symbol used for string representation.

    Methods:
        __init__(self, width=0, height=0):
            Initializes new Rectangle instance with optional width&height.

        area(self):
            Calculates and returns the area of the rectangle.

        perimeter(self):
            Calculates and returns the perimeter of the rectangle.
            If width or height is equal to 0, the perimeter is 0.

        __str__(self):
            Returns string representation of the rectangle using print_symbol.
            If width or height is equal to 0, returns an empty string.

        __repr__(self):
            Returns string repr of rect to recreate new instance using eval().

        __del__(self):
            Prints a farewell message when an instance of Rectangle is deleted.

        @staticmethod
        bigger_or_equal(rect_1, rect_2):
            Returns the biggest rectangle based on the area.
            rect_1 must be an instance of Rectangle.
            rect_2 must be an instance of Rectangle.
            Returns rect_1 if both have the same area value.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle instance with optional width&height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
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
        """Gets the height of the rectangle."""
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
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        If width or height is equal to 0, the perimeter is 0.
        """
        return 2 * (self.__width + self.__height)\
            if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """Returns string repre of rectangle using the print_symbol.

        If width or height is equal to 0, returns an empty string.
        """
        return "\n"\
            .join([str(self.print_symbol) * self.__width] * self.__height)\
            if self.__width > 0 and self.__height > 0 else ""

    def __repr__(self):
        """Returns string repr of rect to recreate new instance -> eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints farewell message when instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): An instance of Rectangle.
            rect_2 (Rectangle): Another instance of Rectangle.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle:
            The rectangle with the larger area.
            If both have the same area value, returns rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
