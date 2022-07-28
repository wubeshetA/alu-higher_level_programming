#!/usr/bin/python3
"""A script to insert a new text after a specifc line of text"""


def append_after(filename="", search_string="", new_string=""):
    '''module Search and update
    '''
    with open(filename, 'r+') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(lines))
