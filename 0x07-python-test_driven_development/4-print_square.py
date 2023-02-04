#!/usr/bin/python3
"""Print a square with the character #."""


def print_square(size):
    """Print a square with the character #.

    Args:
    size: the size length of the square.

    Raises:
    TypeError: if size is not an integer
    ValueError: if size is zero(0)
    TypeError: if size is float and size < 0
    """
    if (type(size) in [float]):
        if (size < 0):
            raise TypeError("size must be an integer")
        size = int(size)

    if (not isinstance(size, (int))):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
