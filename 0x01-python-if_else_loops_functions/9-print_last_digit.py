#!/usr/bin/python3

# Function gets the last digit of a number

def print_last_digit(number):
    if number < 0:
        i = number % (-10)
        print(-(i), end="")
    else:
        i = number % 10
        print((i), end="")
    return abs(i)
