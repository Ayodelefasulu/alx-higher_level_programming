class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle instance\
            with optional width and height.

        @property
        width(self):
            Getter method for the width attribute.

        @width.setter
        width(self, value):
            Setter method for the width attribute.
            Raises:
                TypeError: If width is not an integer.
                ValueError: If width is less than 0.

        @property
        height(self):
            Getter method for the height attribute.

        @height.setter
        height(self, value):
            Setter method for the height attribute.
            Raises:
                TypeError: If height is not an integer.
                ValueError: If height is less than 0.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
