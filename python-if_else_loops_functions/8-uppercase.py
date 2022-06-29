#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 123:
            upper = chr(ord(letter) - 32)
            letter = upper
        print("{}".format(letter), end='')
    print()
