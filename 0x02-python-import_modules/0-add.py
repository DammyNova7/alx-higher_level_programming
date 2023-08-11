#!/usr/bin/python3

# Import a user defined module
from add_0 import add

# variable assignments
a = 1
b = 2
result = add(a, b)

# prints the result using string format
print("{} + {} = {}".format(a, b, result))

# prevents code from executing when imported in another py program
if __name__ == "__main__":
    import sys
    sys.argv[0]
