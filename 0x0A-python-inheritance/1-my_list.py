#!/usr/bin/python3
"""Module that print a sorted
version of an inherited list
"""

class MyList(list):
    """class the returns a sorted list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
