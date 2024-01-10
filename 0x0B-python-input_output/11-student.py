#!/usr/bin/python3
"""This module is an improvement on 10-student module"""


class Student:
    """
    Class representing a student with public instance attributes
    and methods for JSON serialization and deserialization.
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list):
                List of strings representing attribute names to be retrieved.
                If None, all attributes are retrieved.

        Returns:
            dict:
                Dictionary representing the JSON-serializable
                structure of the Student instance.
        """

        # Get all attributes of the instance
        attributes = self.__dict__

        # If attrs is specified, filter attributes based on the provided list
        if attrs is not None and isinstance(attrs, list):
            json_dict = {k: v for k, v in attributes.items() if k in attrs}
        else:
            json_dict = attributes

        return json_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of Student instance based on provided dict.

        Args:
            json (dict):
                Dictionary representing attribute values for Student instance.
        """
        # Update attributes based on the provided dictionary
        self.__dict__.update(json)
