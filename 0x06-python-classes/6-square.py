#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """This is a square class with a size private attribute
    It implements a type check to enure that the ize attribute
    is a valid integer
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (not isinstance(position, tuple) \
                or len(position) != 2 \
                or not all(isinstance(i, int) for i in position) \
                or not all(i > 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) \
                or len(position) != 2 \
                or not all(isinstance(i, int) for i in position) \
                or not all(i > 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#", * self.__size)
