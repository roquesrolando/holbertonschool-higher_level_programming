#!/usr/bin/python3
def best_score(a_dictionary):
    top = ""
    score = 0
    if a_dictionary is None:
        return None
    for i, j in a_dictionary.items():
        if j > score:
            score = j
            top = i
    return top
