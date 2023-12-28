#!/usr/bin/python3
"""Module that creates a rectangle \
        It inherits from the BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Class that creates a rectangle \
            from BaseGeometry class"""

    def __init__(self, width, height):
        if integer_validator("width", width):
            self.__width = width
        if integer_validator("height", height):
            self.__height = height
