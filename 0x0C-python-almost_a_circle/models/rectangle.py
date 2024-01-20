#!/usr/bin/python3
"""This is a Rectangle module. It inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from base.

    It uses the constructor of the base class through the super class function,
    it inherit the argument and adds its own arguments
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function inherits attributes from super class"""

        """
           Attributes:__width, __height, __x, __y

           Return: None

           Getters: getter__width, getter__height, getter__x, getter__y

           Setters: setter__width, setter__height, setter___x, setter__y

           Raises: TypeError, ValueError

           Method(s):
               def area(self):
                   return self.__width * self.__height
        """
        super().__init__(id)

        # Assign arguments to the right attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        """getter for the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """getter for the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        """getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        """getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle of instance"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the character '#'."""

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Prints a string representation of object"""

        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args, **kwargs):
        """Assign args to id, width, height, x, & y  using *args & **kwargs."""

        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for index, value in enumerate(args):
                setattr(self, attributes[index], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""

        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
