#!/usr/bin/python3
for d in range(0, 10):
    for n in range(0, 10):
        if d == 8 and n == 9:
            print("{:d}{:d}".format(d, n))
            break
        elif n > d:
            print("{:d}{:d}, ".format(d, n), end="")
