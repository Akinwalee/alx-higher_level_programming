#!/usr/bin/python3
"""Base Madule for diferent classes"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
