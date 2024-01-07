"""Module: 7-rectangle

This module defines the Rectangle class, representing a geometric rectangle.

Classes:
    Rectangle:
        A class that defines a rectangle by specifying its width and height. It
        provides properties and methods to access and modify these attributes,
        ensuring they adhere to specific constraints.

Attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    number_of_instances (int): The number of instances of Rectangle.
    print_symbol (str or any): The symbol used for string representation.

Methods:
    __init__(self, width=0, height=0):
        Initializes a new Rectangle instance with optional width and height.

    @property
    width(self):
        Retrieves the width of the rectangle.

    @width.setter
    width(self, value):
        Sets the width of the rectangle.
        Args:
            value (int): The width value to set.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.

    @property
    height(self):
        Retrieves the height of the rectangle.

    @height.setter
    height(self, value):
        Sets the height of the rectangle.
        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.

    area(self):
        Computes and returns the rectangle area.

    perimeter(self):
        Computes and returns the rectangle perimeter.
        If width or height is equal to 0, perimeter is equal to 0.

    __str__(self):
        Returns a string representation of the rectangle using
        the symbol(s) stored in print_symbol.
        If width or height is equal to 0, returns an empty string.

    __repr__(self):
        Returns a string representation of the rectangle object
        to be able to recreate a new instance.

    __del__(self):
        Prints "Bye rectangle..." when instance of Rectangle is deleted.

Class Attributes:
    number_of_instances (int): Initialized to 0.
    Incremented during each new instance instantiation.
                              Decremented during each instance deletion.
    print_symbol (str or any): Initialized to "#".
    Used as symbol for string representation. Can be any type.

Example:
    Creating an instance of Rectangle:
    ```python
    my_rectangle = Rectangle(width=5, height=10)
    ```

    Customizing print_symbol for an instance:
    ```python
    my_rectangle.print_symbol = "&"
    ```

    Customizing print_symbol for all instances:
    ```python
    Rectangle.print_symbol = "C"
    ```

Note:
    This module extends the functionality of the Rectangle class,
    introducing public class attributes `number_of_instances` and
    `print_symbol`. The `print_symbol` attribute is used
    as the symbol for string representation in the __str__ method.

"""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int): A count of the number of
        instances of the Rectangle class.
        print_symbol (any): The symbol used for string representation.

    Methods:
        __init__(self, width=0, height=0):
            Initializes new Rectangle instance with optional width&height.

        area(self):
            Calculates and returns the area of the rectangle.

        perimeter(self):
            Calculates and returns the perimeter of the rectangle.
            If width or height is equal to 0, the perimeter is 0.

        __str__(self):
            Returns string representation of rectangle using print_symbol.
            If width or height is equal to 0, returns an empty string.

        __repr__(self):
            Returns string repr of rect to recreate new instance using eval().

        __del__(self):
            Prints farewell message when an instance of Rectangle is deleted.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle instance with optional width&height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

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
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

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

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        If width or height is equal to 0, the perimeter is 0.
        """
        return 2 * (self.__width + self.__height)\
            if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """Returns string repr of rectangle using the print_symbol.

        If width or height is equal to 0, returns an empty string.
        """
        return "\n"\
            .join([str(self.print_symbol) * self.__width] * self.__height)\
            if self.__width > 0 and self.__height > 0 else ""

    def __repr__(self):
        """Returns string repr of rect to recreate new instan using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints farewell message when instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
