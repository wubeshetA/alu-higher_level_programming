#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if number < 0:
    last_digit = ((-1 * number) % 10) * -1

if int(last_digit) > 5:
    print("Last digit of {:d} is {:d}".format(number, last_digit), end=" ")
    print("and is greater than 5")

elif int(last_digit) == 0:
    print("Last digit of {:d} is {:d}".format(number, last_digit), end=" ")
    print("and is 0")

elif int(last_digit) < 6:

    print("Last digit of {:d} is {:d}".format(number, last_digit), end=" ")
    print("and is less than 6 and not 0")
