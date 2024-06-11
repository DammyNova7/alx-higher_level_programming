#!/usr/bin/python3

# function prints a matrix

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(n) for n in row))