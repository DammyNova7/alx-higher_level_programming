#!/usr/bin/python3

def element_at(my_list, idx):
    n = len(my_list)
    if idx < 0:
        return None
    elif idx >= n:
        return None
    else:
        for i in range(n + 1):
            if i == idx:
                return my_list[i]
