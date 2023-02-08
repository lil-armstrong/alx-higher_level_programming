#!/usr/bin/python3

"""Read file"""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout

    Args:
    filename: Name of file to read from    
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
