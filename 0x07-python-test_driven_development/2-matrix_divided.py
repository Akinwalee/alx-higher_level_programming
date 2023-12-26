#!/usr/bin/python3
"""A module that divides a matrix"""


def matrix_divided(matrix, div):
    """This is a function that divides a matrix by div
    and returns an new matrix rounded to 2 decimal places
    """
    for row in matrix:
        if not isinstance(row, list) or \
                not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                    )
    mat_len = len(matrix[0])
    for x in matrix:
        if len(x) != mat_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in x:
            new_elem = round(elem/div, 2)
            new_row.append(new_elem)
        new_matrix.append(new_row)

    return (new_matrix)
