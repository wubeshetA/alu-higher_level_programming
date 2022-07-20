#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total_print = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            total_print += 1
        print()
    except IndexError:
        print()
    finally:
        return total_print
