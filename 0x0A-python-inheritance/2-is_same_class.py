#!/usr/bin/python3
"""Function that returns true if a passed
object is exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """Returns true if a_class is an instance of obj"""

    return (isinstance(a_class, obj))
