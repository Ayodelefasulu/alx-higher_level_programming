#!/usr/bin/python3
"""This module defines a class of students"""


class Student:
    """
    Class representing student with public instance attributes&to_json method.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary repr JSON-serializable struct of Student instance.
        """
        # Get all attributes of the instance
        attributes = self.__dict__

        # Iterate through the attributes and create a dictionary
        json_dict = {}
        for key, value in attributes.items():
            # Check if the attribute is serializable
            if isinstance(value, (str, int)):
                json_dict[key] = value

        return json_dict
