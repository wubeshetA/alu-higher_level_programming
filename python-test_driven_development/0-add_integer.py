#!/usr/bin/python3
"""
module with add function
"""


def add_integer(a, b=98):
    """
    add function
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
