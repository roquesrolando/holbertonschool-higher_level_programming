#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = ((number * -1) % 10) * -1

str1 = "Last digit of {:d} is {:d}".format(number, lastdigit)

if lastdigit > 5:
    str2 = "and is greater than 5"
elif lastdigit == 0:
    str2 = "and is 0"
elif lastdigit < 6 and lastdigit != 0:
    str2 = "and is less than 6 and not 0"
str = str1 + " " + str2
print(str)
