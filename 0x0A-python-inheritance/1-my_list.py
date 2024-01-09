#!/usr/bin/python3
"""Module defining the MyList class."""


class MyList(list):
    """
    MyList class that inherits from list.

    Public instance method:
    - def print_sorted(self): prints the list sorted in ascending order.
    """

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
