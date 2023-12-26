#!/usr/bin/python3
"""A module that prints the character representation
of a shape"""


def print_square(size):
    """Prints a square with the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end="" if y < size - 1 else "\n")
