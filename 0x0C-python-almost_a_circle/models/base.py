#!/usr/bin/python3
"""This is a base Module.

This module is made up of class Base which is ...
...the root class in this project.

"""
import json


class Base:
    """This class contains private class attribute and
    __init__ function.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ function that creates instance of class with id attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""

        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""

        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)
