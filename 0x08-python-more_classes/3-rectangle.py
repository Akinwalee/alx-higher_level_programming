#!/usr/bin/python3

"""
This is a class that demostrates OOP in python

It calculates the area, perimeter, and prints the #
representation of the rectangle
"""


class Rectangle:
    """A class of Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width != 0 and self.__height != 0:
            return (2 * (self.__width + self.__height))
        else:
            return (0)

    def __str__(self):
        """Return a # representation of rectangle"""
        output = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    output += "#"
                output += '\n'
            return (output.rstrip())
        else:
            return (output)
