#!/usr/bin/python3

"""Class to JSON"""


def class_to_json(obj):
    """Convert a class to JSON.

    Args:
    obj: Class object

    Returns:
    Return the dictionaty description with simple data structure \
     of the object
    """
    return obj.__dict__
