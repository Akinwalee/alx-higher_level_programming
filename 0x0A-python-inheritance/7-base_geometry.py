#!/usr/bin/python3
"""A Geometry Modules for different \
        gemetric shapes"""


class BaseGeometry:
    """Base class for different geometric shapes"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
