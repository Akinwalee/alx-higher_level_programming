#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rang = len(array) - 1
    for array in matrix:
        for x, i in enumerate(array):
            print("{:d}{}".format(i, " " if x < rang else '\n'), end="")
