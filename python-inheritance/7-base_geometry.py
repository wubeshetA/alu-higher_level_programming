#!/usr/bin/python3
"""Geometry class"""


class BaseGeometry:
    """represent a geometry"""

    def area(self):
        """raise area not implemented exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
