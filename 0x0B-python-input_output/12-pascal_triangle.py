#!/usr/bin/python3
'''returns a list of pascal triangle'''


def pascal_triangle(n):
    '''returns a list of pascal triangle'''

    lists = [[]]
    if n == 0:
        lists.append(1)
        return lists

    for x in range(1, n):
        pascal = []
        for i in range(x + 1):
            if i == 0:
                pascal.append(1)
                continue
            if i == x:
                pascal.append(1)
                continue
            pascal.append(lists[x - 1][i - 1] + lists[x - 1][i])
        lists.append(pascal)
    return lists
