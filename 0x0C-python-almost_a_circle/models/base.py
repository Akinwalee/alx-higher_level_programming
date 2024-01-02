#!/usr/bin/python3
"""Base Madule for diferent classes"""


class Base:
    """Base class for all classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
