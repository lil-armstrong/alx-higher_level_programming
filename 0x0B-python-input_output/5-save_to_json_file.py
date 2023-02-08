#!/usr/bin/python3
"""Save object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file as JSON

    Args:
    my_obj: Python object
    filename: File name to write to

    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f, sort_keys=True)
