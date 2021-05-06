#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    value = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, 
            "D": 500, "M": 1000}
    for i in roman_string:
        for j, z in roman.items():
            if i == j:
                value += z
    return value
