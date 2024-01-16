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

          Methods: validate_integer, validate_positive, validate_non_negative

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
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.validate_non_negative("y", value)
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, attribute_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def validate_positive(self, attribute_name, value):
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative(self, attribute_name, value):
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
