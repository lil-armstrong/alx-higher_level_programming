#!/usr/bin/python3

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed

    Args:
    a: integer or float
    b: integer or float

    Raises:
    TypeError: if either a or b is non-integer or non-float
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")

    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
