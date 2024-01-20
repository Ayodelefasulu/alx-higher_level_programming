#!/usr/bin/python3
"""This is a base Module.

This module is made up of class Base which is ...
...the root class in this project.

"""
import json
import csv
from turtle import Turtle, Screen


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
        js_string = cls.\
            to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(js_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string."""

        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set."""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square
        else:
            return None

        dummy_instance.update(**dictionary)  # Update with real values
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from the JSON file."""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV file."""

        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize from CSV file and return a list of instances."""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                dictionaries =\
                    [dict(zip(cls.csv_attributes, map(int, row))) for row in reader]
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the rectangles and squares using Turtle graphics."""

        # Create a Turtle screen
        screen = Screen()
        screen.bgcolor("white")

        # Create a Turtle object
        drawer = Turtle()
        drawer.speed(2)

        # Draw rectangles
        for rect in list_rectangles:
            drawer.penup()
            drawer.goto(rect.x, rect.y)
            drawer.pendown()
            drawer.forward(rect.width)
            drawer.right(90)
            drawer.forward(rect.height)
            drawer.right(90)
            drawer.forward(rect.width)
            drawer.right(90)
            drawer.forward(rect.height)
            drawer.right(90)

        # Draw squares
        for square in list_squares:
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            for _ in range(4):
                drawer.forward(square.size)
                drawer.right(90)

        # Close the window on click
        screen.exitonclick()
