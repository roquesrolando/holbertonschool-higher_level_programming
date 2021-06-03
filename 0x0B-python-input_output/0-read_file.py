#!/usr/bin/python3

def read_file(filename=""):

    with open(filename, encoding='UTF8') as f:
        for i in f:
            print(i, end='')
