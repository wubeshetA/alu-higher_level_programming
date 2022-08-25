#!/usr/bin/python3
import unittest
from models.base import Base

"""
Unittests for Base class
"""


class TestBase(unittest.TestCase):
    """
    Class of functions to run tests
    """
    def setUp(self):
        """
        setup Base class
        """
        pass

    def tearDown(self):
        """
        tearDown tests
        """
        pass

    def test_id(self):
        """
        Test id
        """

        b1 = Base()
        b2 = Base()
        b3 = Base(98)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 98)
        self.assertEqual(b4.id, 4)
