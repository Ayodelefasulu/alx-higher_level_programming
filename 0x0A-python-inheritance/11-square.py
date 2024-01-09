#!/usr/bin/python3
"""Module defining the Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition for Square, inherits from Rectangle."""

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)

        # Call constructor of parent class with width&height both set to size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] {}/{}"\
            .format(self._Rectangle__width, self._Rectangle__height)
