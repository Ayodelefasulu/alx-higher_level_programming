import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rectangle = Rectangle(width=10, height=20, x=5, y=8, id=1)

        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 8)
        self.assertEqual(rectangle.id, 1)

    def test_setters_and_getters(self):
        rectangle = Rectangle(width=10, height=20, x=5, y=8)

        # Test valid attribute values
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

        rectangle.x = 10
        self.assertEqual(rectangle.x, 10)

        rectangle.y = 15
        self.assertEqual(rectangle.y, 15)

        # Test invalid attribute values
        with self.assertRaises(TypeError):
            rectangle.width = "invalid"
        with self.assertRaises(ValueError):
            rectangle.width = 0

        with self.assertRaises(TypeError):
            rectangle.height = "invalid"
        with self.assertRaises(ValueError):
            rectangle.height = -5

        with self.assertRaises(TypeError):
            rectangle.x = "invalid"
        with self.assertRaises(ValueError):
            rectangle.x = -2

        with self.assertRaises(TypeError):
            rectangle.y = "invalid"
        with self.assertRaises(ValueError):
            rectangle.y = -3

if __name__ == '__main__':
    unittest.main()
