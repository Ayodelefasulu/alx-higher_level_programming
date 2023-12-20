#!/usr/bin/python3

class Square:
    """This is a square class."""
    def __init__(self, size):
        """Instantiates a square with size ``size``.

        Args:
            size (int): The size of the square

        Note:
            The size attribute is private, and its modified to
            include the class name to make it private, name mangling.
        """
        self.__size = size
