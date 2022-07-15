#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy_list.append(replace)
            continue
        copy_list.append(my_list[i])
    return copy_list
