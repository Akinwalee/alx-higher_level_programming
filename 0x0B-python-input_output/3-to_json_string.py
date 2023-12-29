#!/usr/bin/python3
import json
"""Module that serializes an object"""


def to_json_string(my_obj):
    """Returns the json representation of my_obj"""
    return (json.dumps(my_obj))
