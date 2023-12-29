#!/usr/bin/python3
"""Writes an Object to a text file as JSON"""


import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj as JSON to filename"""
    with open(filename, "a+", encoding="utf-8") as f:
        json.dump(my_obj, f)
