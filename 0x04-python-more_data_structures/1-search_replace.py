#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new = my_list.copy()
        for i in range(len(my_list)):
            if search == 0:
                new[0] = replace
            elif i == search - 1:
                new[i] = replace
        return new
