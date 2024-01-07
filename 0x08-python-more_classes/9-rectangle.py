#!/usr/bin/python3
"""Module: 9-rectangle

Description:
    Defines a rectangle with width, height, and additional features.

Class:
    Rectangle:
        A class that defines a rectangle.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

Class Attributes:
    number_of_instances (int):
    A count of the number of instances of the Rectangle class.
    print_symbol (any): The symbol used for string representation.
    Initialized to '#'.

Methods:
    __init__(self, width=0, height=0):
        Initializes new Rectangle instance with optional width&height.

    area(self):
        Calculates and returns the area of the rectangle.

    perimeter(self):
        Calculates and returns the perimeter of the rectangle.
        If width or height is equal to 0, the perimeter is 0.

    __str__(self):
        Returns string repre of the rectangle using print_symbol.
        If width or height is equal to 0, returns an empty string.

    __repr__(self):
        Returns string repr of rect to recreate new instance -> eval().

    __del__(self):
        Prints farewell message when instance of Rectangle is deleted.

    @staticmethod
    bigger_or_equal(rect_1, rect_2):
        Returns the biggest rectangle based on the area.
        rect_1 must be an instance of Rectangle.
        rect_2 must be an instance of Rectangle.
        Returns rect_1 if both have the same area value.

    @classmethod
    square(cls, size=0):
        Returns a new Rectangle instance with width == height == size.

Example:
    Example usage is provided at the end of the module.

Note:
    All instance and class attributes are private.
"""


class Rectangle:
    """Defines rectangle with width, height, and additional features."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes new Rect instance with optional width&height."""
        self.__width = 0
        self.__height = 0
        Rectangle.number_of_instances += 1

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)\
            if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """Return string repr of rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + "\n")\
            * self.__height

    def __repr__(self):
        """Return string repr of rect to recreate new instance ->eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print farewell message when instance of Rect is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
