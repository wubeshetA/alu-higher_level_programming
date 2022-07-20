#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) != int:
                continue
            else:
                print("{:d}".format(my_list[i]), end="")
                print_count += 1
        print()
        return print_count
    except TypeError:
        pass
