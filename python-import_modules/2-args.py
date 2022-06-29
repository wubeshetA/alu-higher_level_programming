#!/usr/bin/python3
import sys
args = sys.argv[1:]
args_len = len(args)
if args_len == 0:
    print("0 arguments.")
elif args_len == 1:
    print("1 argument:\n1: {}".format(args[0]))
else:
    print("{:d} arguments:".format(args_len))
    for i in range(args_len):
        print("{:d}: {}".format(i + 1, args[i]))
