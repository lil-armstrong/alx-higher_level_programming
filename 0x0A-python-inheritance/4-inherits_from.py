#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class\
    that inherited (directly or indirectly) from\
    a specified class.

    Args:
    obj: Object instance to check
    a_class: specified class

    Returns:
    True: if object is an instance
    False: otherwise
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        False
