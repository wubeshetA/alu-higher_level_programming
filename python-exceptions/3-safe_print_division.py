#!/usr/bin/python3
from decimal import DivisionByZero
from unittest import result

from sympy import re


def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
