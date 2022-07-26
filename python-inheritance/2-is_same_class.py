#!/usr/bin/python3
"""A function that check if object is an instance of a class"""


def is_same_class(obj, a_class):
    """ Return True if obj is instance of a_class, otherwise False"""
    return True if type(obj) == a_class else False
