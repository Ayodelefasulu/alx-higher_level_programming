#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 8, 12]), 12)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -8]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -12]), -5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -3, 4, 2]), 4)
        self.assertEqual(max_integer([10, -5, 8, -12]), 10)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([7, 7, 7, 5, 7]), 7)


if __name__ == '__main__':
    unittest.main()
