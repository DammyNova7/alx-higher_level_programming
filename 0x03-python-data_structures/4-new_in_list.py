#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    size = len(my_list)
    copy = my_list[:]

    if idx < 0:
        return (my_list)
    elif idx >= size:
        return (my_list)
    else:
        for i in range(size + 1):
            if i == idx:
                copy[i] = element
    return (copy)
