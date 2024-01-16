import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
from io import StringIO

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

    # Test for "#"
    def test_display(self):
        r1 = Rectangle(4, 6)

        # Redirect stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r1.display()
            output = mock_stdout.getvalue().strip()

        expected_output = "####\n####\n####\n####\n####\n####"
        self.assertEqual(output, expected_output)

    def test_display_with_height_2(self):
        r1 = Rectangle(2, 2)

        # Redirect stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r1.display()
            output = mock_stdout.getvalue().strip()

        expected_output = "##\n##"
        self.assertEqual(output, expected_output)


    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)

        # Redirect stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(r1)
            output = mock_stdout.getvalue().strip()

        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(output, expected_output)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)

        # Redirect stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(r1)
            output = mock_stdout.getvalue().strip()

        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(output, expected_output)

    def test_str_with_default_values(self):
        r2 = Rectangle(5, 5, 1)

        # Redirect stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(r2)
            output = mock_stdout.getvalue().strip()

        expected_output = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(output, expected_output)

    def test_dislay_with_shifted_position(self):
        r2 = Rectangle(3, 2, 1, 0)
        tst = r2.display()
        exp = "  ##\n  ##\n  ##"
        self.assetEqual(tst, exp)


if __name__ == '__main__':
    unittest.main()

