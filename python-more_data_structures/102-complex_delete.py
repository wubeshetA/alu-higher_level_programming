#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_dict = {}
    if value in a_dictionary.values():

        for key, v in a_dictionary.items():
            if a_dictionary[key] == value:
                continue
            copy_dict[key] = v
        a_dictionary = copy_dict
        return a_dictionary
    else:
        return a_dictionary
