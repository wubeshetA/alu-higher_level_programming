#!/usr/bin/python3
"""
module with add function
"""


def add_integer(a, b=98):
    """
    Return integer addtion of a and b
    Rasises:
        TypeError: If either of a or b is a non-integer and not-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
