#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in my_list:
        if i == search - 1:
            new[i] = replace
    return new
