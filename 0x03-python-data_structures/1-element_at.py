#!/usr/bin/python3
# Function that retrieves an element from a list like in C.
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return (None)
    else:
        for i in my_list[idx:idx + 1]:
            return (i)
