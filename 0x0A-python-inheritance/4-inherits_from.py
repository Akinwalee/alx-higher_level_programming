#!/usr/bin/python3
"""Function that returns true if a passed \
        object is a subclass of a specified class"""


def inherits_from(obj, a_class):
    """Returns true if obj is a subclass of a_class"""

    return (type(obj) == a_class)
