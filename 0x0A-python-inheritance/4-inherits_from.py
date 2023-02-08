#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class\
    that inherited (directly or indirectly) from\
    a specified class.

    Args:
    obj (any): Object instance to check
    a_class (type): The class to match the type of obj to.

    Returns:
    True: if object is an instance
    False: otherwise
    """
    return issubclass(obj.
                      __class__, a_class) and type(obj) != a_class
