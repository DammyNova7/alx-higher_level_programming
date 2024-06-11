#!/usr/bin/python3

# function adds up tuples and return a tuple

def add_tuple(tuple_a=(), tuple_b=()):
    a_list = list(tuple_a)
    b_list = list(tuple_b)
    new_list = []
    if len(a_list) < 2 or len(b_list) < 2:
        a_list = a_list + [0] * (2 - len(a_list))
        b_list = b_list + [0] * (2 - len(b_list))
        new_list.append(a_list[0] + b_list[0])
        new_list.append(a_list[1] + b_list[1])
    elif len(a_list) > 2 or len(b_list) > 2:
        new_list.append(a_list[0] + b_list[0])
        new_list.append(a_list[1] + b_list[1])
    else:
        new_list.append(a_list[0] + b_list[0])
        new_list.append(a_list[1] + b_list[1])

    return (tuple(new_list))
