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

          Methods:
              def area(self):
                  return self.__width * self.__height

          Raises: TypeError, ValueError

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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.height)
