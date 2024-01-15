#!/usr/bin/python3
"""This is a base Module.

This module is made up of class Base which is ...
...the root class in this project.

"""


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
