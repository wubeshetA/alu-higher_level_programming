#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main(argv):
    args = argv[1:]
    args_len = len(args)
    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[1] != '+' and args[1] != '-' and args[1] != '*' and args[1] != '/':
        print("operator: %s" % args[1])
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    a = int(args[0])
    b = int(args[2])
    operator = args[1]
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    import sys
    main(sys.argv)
