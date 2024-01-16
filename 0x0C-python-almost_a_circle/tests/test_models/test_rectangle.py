import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rectangle = Rectangle(width=10, height=20, x=5, y=8, id=1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 8)
        self.assertEqual(rectangle.id, 1)
    def test_setters_and_getters(self):
        rectangle = Rectangle(width=10, height=20, x=5, y=8, id=1)

    # Test width
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)
    # Test height
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

    # Test x
        rectangle.x = 10
        self.assertEqual(rectangle.x, 10)

    # Test y
        rectangle.y = 15
        self.assertEqual(rectangle.y, 15)

    def test_inheritance(self):
        rectangle = Rectangle(width=10, height=20, x=5, y=8, id=1)

    # Test if it inherits from Base
        self.assertIsInstance(rectangle, Base)

    # Test for area of rectangle
    def test_area(self):
        rectangle = Rectangle(10, 20, 3, 4, 5)
        self.assertEqual(rectangle.area(), 200)

        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.area(), 2)

        rectangle = Rectangle(8, 3, 3, 4, 5)
        self.assertEqual(rectangle.area(), 24)

        rectangle = Rectangle(15, 1, 3, 4, 5)
        self.assertEqual(rectangle.area(), 15)

        rectangle = Rectangle(2, 22, 3, 4, 5)
        self.assertEqual(rectangle.area(), 44)


if __name__ == '__main__':
        unittest.main()
