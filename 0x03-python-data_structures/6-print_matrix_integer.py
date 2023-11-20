#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        rang = len(array) - 1
        for x, i in enumerate(array):
            print("{:d}{}".format(i, " " if x < rang else '\n'), end="")
    if not matrix:
        print("Hello\n")
