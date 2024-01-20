#!/usr/bin/python3
"""This module inherits from rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """This class inherits from the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the constructor"""

        # Call the super class constructor with id, x, y, width, and height
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter that returns the width of the square"""

        return self.width  # size is the same as width for a Square

    @size.setter
    def size(self, value):
        """Setter sets width and heigth of square"""

        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
