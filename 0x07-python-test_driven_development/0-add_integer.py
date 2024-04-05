#!/usr/bin/python3

def add_integer(a, b=98):
    n = isinstance(a, int) or isinstance(a, float)
    m = isinstance(b, int) or isinstance(b, float)

    if not n:
        raise TypeError("a must be an integer")
    if not m:
        raise TypeError("b must be an integer")

    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return (a + b)

print(add_integer(2, 3.5))
