#!/usr/bin/python3
# Function that retrieves an element from a list like in C.
def element_at(my_list, idx):
    length = len(my_list)
    i = 0
    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        while i != idx:
            i += 1
            if i == idx:
                return (my_list[i])
