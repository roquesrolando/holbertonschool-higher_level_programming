#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is not None or ser_2 is not None:
        elements = []
        for i in set_1:
            for j in set_2:
                if i == j:
                    elements += j
        return set(elements)
