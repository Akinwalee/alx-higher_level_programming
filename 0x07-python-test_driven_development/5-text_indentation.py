#!/usr/bin/python3
"""Module that prints a text"""


def text_indentation(text):
    """Function that prints a text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for x in text:
        print("{}".format(x), end="\n\n" if x in ["?", ":", "."] else '')
