#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2 or len_b < 2:
        if len_a == 1:
            tuple_a_1 = tuple_a[0]
            tuple_a_2 = 0
        elif len_a == 0:
            tuple_a_1 = 0
            tuple_a_2 = 0
        if len_b == 1:
            tuple_b_1 = tuple_b[0]
            tuple_b_2 = 0
        elif len_b == 0:
            tuple_b_1 = 0
            tuple_b_2 = 0
    if len_a >= 2:
        tuple_a_1 = tuple_a[0]
        tuple_a_2 = tuple_a[1]

    if len_b >= 2:
        tuple_b_1 = tuple_b[0]
        tuple_b_2 = tuple_b[1]

    i = tuple_a_1 + tuple_b_1
    j = tuple_a_2 + tuple_b_2

    new_tuple = (i, j)
    return new_tuple
