#!/usr/bin/python3

def print_square(size):
    """Print a square with the character #.

    Args:
    size: the size length of the square.
    """
    if (not isinstance(size, (int))):
        raise TypeError("size must be an integer")
    elif (size <= 0):
        raise TypeError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
