#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            letter = chr(ord(str[i]) - 32)
            new += letter
        else:
            new += str[i]

    print("{:s}".format(new))
