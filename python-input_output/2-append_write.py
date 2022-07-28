#!/usr/bin/python3
"""A function that appends a string a file"""


def append_write(filename="", text=""):
    """Appends a string to a file"""

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
