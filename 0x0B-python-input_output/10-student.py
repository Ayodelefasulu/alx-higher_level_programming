class Student:
    """
    Class representing a student with public instance attributes and
    ...a to_json method.
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
            dict: A dictionary representing the JSON-serializable structure
                of the Student instance.
        """
        # Get all attributes of the instance
        attributes = self.__dict__

        # If attrs is specified, filter attributes based on the provided list
        if attrs is not None and isinstance(attrs, list):
            json_dict =\
                {key: value for key, value in attributes.items() if key in attrs}
        else:
            json_dict = attributes

        return json_dict
