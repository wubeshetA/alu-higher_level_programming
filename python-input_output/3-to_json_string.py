#!/usr/bin/python3
"""A function that returns JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Converts an object to json"""
    return json.dump(my_obj)
