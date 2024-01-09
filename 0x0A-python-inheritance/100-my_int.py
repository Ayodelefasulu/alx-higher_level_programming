#!/usr/bin/python3
"""Module defining the MyInt class."""


class MyInt(int):
    """Class definition for MyInt, inherits from int."""

    def __eq__(self, other):
        """Override the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        return super().__eq__(other)
