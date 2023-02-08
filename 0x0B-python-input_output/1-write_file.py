#!/usr/bin/python3

"""Write to file"""


def write_file(filename="", text=""):
    """Write a string to a text file\
    Returns the number of characters written

    Args:
    filename (str): File name
    text (str): Text string to write to file

    Returns:
    (int) The number of characters written
    """
    nwrite = 0
    with open(filename, "w") as f:
        nwrite = f.write(text)

    return (nwrite)
