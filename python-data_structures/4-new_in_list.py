#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list
    if idx < 0 or idx >= len(my_list):
        return copy_list
    copy_list = my_list.insert(idx, copy_list)
    return copy_list
