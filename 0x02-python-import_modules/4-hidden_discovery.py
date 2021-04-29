#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    files = dir(hidden_4)
    length = len(files)
    for d in range(length):
        if files[d][1] != "_":
            print("{:s}".format(files[d]))
