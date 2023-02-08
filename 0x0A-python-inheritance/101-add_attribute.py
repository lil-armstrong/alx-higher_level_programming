#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, attr_name, attr_value):
    """Add new attribute to an object

    Args:
    obj (any): Object to add attribute to
    attr_name: Name of attribute to add
    attr_value: Value of attribute to add
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
