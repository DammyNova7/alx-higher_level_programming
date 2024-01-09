#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    size = len(my_list)
    if idx < 0:
        print(my_list)
    elif idx >= size:
        print(my_list)
    else:
        for i in range(size + 1):
            if i == idx:
                my_list[i] = element
    return my_list
