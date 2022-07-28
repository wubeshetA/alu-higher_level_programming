#!/usr/bin/python3
"""Function to read a file"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
