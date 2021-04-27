#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        new = number % 10
    else:
        new = (number * -1) % 10

    print("{:d}".format(new), end='')
    return new
