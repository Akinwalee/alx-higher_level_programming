#!/usr/bin/python3
"""Reads a text file and prints it"""


def read_file(filename=""):
    """Reads filename and prints the content to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
