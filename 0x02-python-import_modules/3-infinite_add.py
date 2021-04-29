#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv
    length = len(arg)
    add = 0
    if length == 0:
        print("0")
    elif length > 0:
        for d in range(1, length):
            add += int(arg[d])
    print("{:d}".format(add))
