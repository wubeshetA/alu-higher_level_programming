#!/usr/bin/python3
""" Test for Base, Rectangle, and Square Class."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test for Base class."""

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_id(self):
        """Test id"""
        b1 = Base()
        b2 = Base()
        b3 = Base(5)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 5)
        self.assertEqual(b4.id, 3)


if __name__ == "__main__":
    unittest.main()
