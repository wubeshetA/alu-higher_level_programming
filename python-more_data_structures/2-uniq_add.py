#!/usr/bin/python3
def uniq_add(my_list=[]):
    mem = []
    for item in my_list:
        if item not in mem:
            mem.append(item)
    sum = 0
    for item in mem:
        sum += item
    return sum
