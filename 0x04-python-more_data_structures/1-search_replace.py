#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for i, n_list in enumerate(new_list):
        if search == n_list:
            new_list[i] = replace
    return (new_list)
