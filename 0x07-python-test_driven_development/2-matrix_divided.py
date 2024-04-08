#!/usr/bin/python3

# matrix must be lists of integers or floats typerror
# each row in the matrix must be of the same size typerror
# divisor must be a number int or float typeerror
# divisor can't be equal to 0 ZerodivisionError
# all elements should be divided by divisor and rounde to 2 decimal places
# return a new matrix

def matrix_divided(matrix, div):
    new_matrix = []
    for row in matrix:
        size = len(matrix[0])
        new_matrix_row = []
        for i in row:
            if div == 0:
                raise ZeroDivisionError("division by zero")
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(row) > size or len(row) < size:
                raise TypeError("Each row of the matrix must have the same size")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            new_matrix_row.append(round(i / div, 2))
        new_matrix.append(new_matrix_row)
    return (new_matrix)
