#!/usr/bin/python3

def add_integer(a, b=98):
    """Add two(2) integers.

    Args:
    a: integer or float
    b: integer or float

    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be a integer")

    if (not isinstance(b, (int, float))):
        raise TypeError("b must be a integer")

    a = int(a)
    b = int(b)

    return (a + b)
