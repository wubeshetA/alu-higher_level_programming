#!/usr/bin/python3
"""A function that finds a pick in a list of integers"""

def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    
    if len(list_of_integers):
                return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    for i in range(len(list_of_integers)):
        
        if i == 0:
            if list_of_integers[0] >= list_of_integers[1]:
                return list_of_integers[0]
        elif i == len(list_of_integers) - 1:
            if list_of_integers[-1] >= list_of_integers[-2]:
                return list_of_integers[-1]
        elif i != 0 and i != len(list_of_integers) - 1:
            if list_of_integers[i] >= list_of_integers[i-1] and list_of_integers[i+1]:
                return list_of_integers[i]
