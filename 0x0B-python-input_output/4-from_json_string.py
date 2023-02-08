#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string

    Args:
    my_str: json string containing Python object

    Returns:
    Python object
    """
    return (json.loads(my_str))
