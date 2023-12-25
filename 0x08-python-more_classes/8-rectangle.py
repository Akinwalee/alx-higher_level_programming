#!/usr/bin/python3

"""
This is a class that demostrates OOP in python

It calculates the area, perimeter, and prints the #
representation of the rectangle
"""


class Rectangle:
    """A class of Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        r = []
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                [r.append(str(self.print_symbol)) for i in range(self.__width)]
                if i != self.__height - 1:
                    r.append("\n")
            return ("".join(r))
        else:
            return ("")

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return (rect_1)
        elif rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)
