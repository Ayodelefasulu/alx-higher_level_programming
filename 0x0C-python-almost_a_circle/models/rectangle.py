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
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


"""     super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.getter
    def x(self, x):
        self.__ = x

    @property
    def y(self):
        return self.__y

    @y.getter
    def y(self, y):
        self.__y = y
"""
