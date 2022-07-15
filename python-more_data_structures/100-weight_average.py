#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    weight = 0
    for numbers in my_list:
        temp_mult = 1

        for i in range(2):
            temp_mult *= numbers[i]
            if i == 1:
                weight += numbers[1]
        sum += temp_mult
    average = sum / weight
    return average
