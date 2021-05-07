#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    total = 0
    for i, j in my_list:
        average += i * j
        total += j
    return average / total
