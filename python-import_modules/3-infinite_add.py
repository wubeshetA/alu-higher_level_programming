#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    sum = 0
    for arg in args:
        sum += int(arg)
    print(sum)


if __name__ == "__main__":
    main()
