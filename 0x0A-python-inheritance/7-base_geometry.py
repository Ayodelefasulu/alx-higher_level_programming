#!/usr/bin/python3
"""Module defining the BaseGeometry class."""


class BaseGeometry:
    """Class definition for BaseGeometry."""

    def area(self):
        """Raises Exception with message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer:
            raises TypeError exception, message: '<name> must be an integer'.
        - If value is less or equal to 0:
            raises ValueError exception, msg: '<name> must be greater than 0'.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
