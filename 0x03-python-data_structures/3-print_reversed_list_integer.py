#!/usr/bin/python3
# Function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
