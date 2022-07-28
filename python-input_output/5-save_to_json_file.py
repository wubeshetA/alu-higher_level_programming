#!/usr/bin/python3
"""A function that writes a JSON representation of an object to a file."""

import json


def save_to_json_file(my_obj, filename):
    """Save a JSON representation of an object to a file."""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
