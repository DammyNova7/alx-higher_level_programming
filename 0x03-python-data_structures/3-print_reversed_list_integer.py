#!/usr/bin/python3
# Function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return (None)
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))