#!/usr/bin/python3
"""Deserializes a JSON string"""


import json


def from_json_string(my_str):
    """Return the the python object representation of my_str"""
    return (json.loads(my_str))
