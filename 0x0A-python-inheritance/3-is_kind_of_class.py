#!/usr/bin/python3
"""Same class or inherit."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of a class\
    or an instance of an object that inherited from a subclass of a_class.

    Args:
    obj: Object instance
    a_class: Specified class

    Returns:
    True: if obj is an instance of ``a_class``
    False: otherwise
    """
    return isinstance(obj, (a_class))
