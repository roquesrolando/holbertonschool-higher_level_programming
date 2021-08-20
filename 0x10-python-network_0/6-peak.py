#!/usr/bin/python3
"""Find a Peak"""


def find_peak(list_of_integers):
    """Finds a peak"""

    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return l[1]

    for idx in range(1, length):
        if (list_of_integers[idx - 1] < list_of_integers[idx] and
           list_of_integers[idx] > list_of_integers[idx + 1]):
            return list_of_integers[idx]

    return list_of_integers[0]
