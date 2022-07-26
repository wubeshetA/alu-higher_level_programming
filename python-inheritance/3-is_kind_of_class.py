#!/usr/bin/python3
''' functin that check if object is instance of class
'''


def is_kind_of_class(obj, a_class):
    '''Return True if obj is a kind of class otherwise False
    obj: an object
    a_class: a class
    Returns: Bool
    '''
    return isinstance(obj, a_class)
