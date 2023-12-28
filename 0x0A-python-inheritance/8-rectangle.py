#!/usr/bin/python3
"""Module that creates a rectangle \
        It inherits from the BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Class that creates a rectangle \
            from BaseGeometry class"""

    def __init__(self, width, height):
        if super().integer_validator(width):
            self.__width = width
        if super().integer_validator(height):
            self.__height = height
