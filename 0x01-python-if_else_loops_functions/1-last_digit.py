#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = ((number * -1) % 10) * -1

if lastdigit > 5:
    print("Last digit of {:d} is {:n} and is greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {:d} is {:n} and is 0".format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {:d} is {:n} and is less than 6 and not 0".format(number, lastdigit))
