#!/usr/bin/python3
"""Module that appends to a text file"""


def append_write(filename="", text=""):
    """Appends text to filename"""

    with open(filename, "a+", encoding="utf-8") as f:
        return (f.write(text))
