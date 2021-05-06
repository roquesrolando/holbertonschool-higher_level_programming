#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    value = 0
    roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    for i in roman_string:
        for j, z in roman.items():
            if i == j:
                if value != 0 and value < z:
                    value -= z
                    if value < 0:
                        value *= -1
                    continue
                value += z
    return value
