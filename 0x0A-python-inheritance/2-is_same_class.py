#!/usr/bin/python3
"""Exact same object."""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
    obj: Object instance
    a_class: Class representation

    Returns:
    True: if object is exactly an instance of a_class
    False: otherwise
    """
    return True if type(obj) is a_class else False
