#!/usr/bin/python3
"""Function that returns true if a passed
object is an instance or subclass of a specified class"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance of a_class"""

    return (issubclass(obj, a_class))
