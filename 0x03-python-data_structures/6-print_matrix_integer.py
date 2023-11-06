#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for x, i in enumerate(array):
            print("{:d}{}".format(i," " if x < (len(array) - 1) else '\n'), end="")
