#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """This is a square class with a size private attribute
    It implements a type check to enure that the ize attribute
    is a valid integer
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
