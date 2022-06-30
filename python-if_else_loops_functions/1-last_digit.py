#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1])
if number < 0:
    last_digit = -last_digit

if int(last_digit) > 5:
    print(f"Last digit of {number:d} is {last_digit:d}", end=" ")
    print("and is greater than 5")

elif int(last_digit) == 0:
    print(f"Last digit of {number:d} is {last_digit:d}", end=" ")
    print("and is 0")

elif int(last_digit) < 6:

    print(f"Last digit of {number:d} is {last_digit:d}", end=" ")
    print("and is less than 6 and not 0")
