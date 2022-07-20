#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            result.append(div)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
            continue
        except TypeError:
            print("wrong type")
            result.append(0)
            continue
        except IndexError:
            print("out of range")
            result.append(0)
            break
    return result
