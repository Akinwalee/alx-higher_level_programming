#!/usr/bin/python3
"""A module that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Returns a list containing
    all attributes of obj
    """

    return (dir(obj))
