#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv
    length = len(arg) - 1

    if length >= 1:
        print(length, "arguments:")
        for d in range(1, length + 1):
            print("{:d}: {}".format(d, arg[d]))
    elif length == 0:
        print("0 arguments")
