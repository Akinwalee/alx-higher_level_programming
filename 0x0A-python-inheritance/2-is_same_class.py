#!/usr/bin/python3
"""Function that returns true if a passed \
        object is exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """Returns true if obj is an instance of a_class"""

   if (type(obj) == type(a_class)):
        return (True)

    return (False)
