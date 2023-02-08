#!/usr/bin/python3

"""Write to file"""


def write_file(filename="", text=""):
    """Write a string to a text file\
    Returns the number of characters written\

    Args: 
    filename: File name
    text: Text string to write to file

    Returns:
        The number of characters written
    """
    nwrite = 0
    with open(filename, "w") as f:
        nwrite = f.write(text)

    return (nwrite)
