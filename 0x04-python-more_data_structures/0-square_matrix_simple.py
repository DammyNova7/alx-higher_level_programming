#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        sub_list = []
        for i in row:
            sub_list.append(i ** 2)
        new_matrix.append(sub_list)
    return (new_matrix)
