import unittest
import sys
# sys.path.insert(0, '../..')
from models.base import Base


class TestBase(unittest.TestCase):
    def test___init__(self):
        b = Base()
        self.assertEqual(b.id, 1)
