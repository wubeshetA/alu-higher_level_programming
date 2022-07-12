#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = [item for item in my_list]
    if idx < 0 or idx >= len(my_list):
        return copy_list
    copy_list[idx] = element
    return copy_list
