#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module that creates a rectangle \
        It inherits from the BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Class that creates a rectangle \
            from BaseGeometry class"""

    def __init__(self, width, height):
        base = BaseGometry()
        base.integer_validator("width", width)
        self.__width = width
        base.integer_validator("height", height)
        self.__height = height
