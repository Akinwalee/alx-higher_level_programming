#!/usr/bin/python3
"""Module that creates squares. \
        It inherits from the Rectangle class"""


Rectangle = __import__('9-rectangle')

class Square(Rectangle):
    """
    Creates a square by modifying methods
    from the Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(self, size)

    def area(self):
        return (self.__size ** 2)
