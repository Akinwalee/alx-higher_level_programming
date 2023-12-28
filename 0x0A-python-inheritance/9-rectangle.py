#!/usr/bin/python3
"""Module that creates a rectangle"""


class Rectangle(BaseGeometry):
    """Class that creates a rectangle \
            from BaseGeometry class"""

    def __init__(self, width, height):
        if super().integer_validator(width):
            self.__width = width
        if super().integer_validator(height):
            self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__():
        return ("[Rectangle] {}/{}".format(width, height))
