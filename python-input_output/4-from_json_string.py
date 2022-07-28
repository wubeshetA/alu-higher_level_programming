#!/usr/bin/python3
"""A function that returns python obect from JSON."""

import json


def from_json_string(my_str):
    return json.loads(my_str)
