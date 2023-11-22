#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """This is a square class with a size private attribute
    It implements a type check to enure that the ize attribute
    is a valid integer
    """

    def __init__(self, size=0):
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
