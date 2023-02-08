#!/usr/bin/python3

"""Append file"""

n_append = 0


def append_write(filename="", text=""):
    """Append a string to a text file \
    returns the number of characters added

        Args:
        filename: File path to write to
        text: Text to write to file

        Returns:
                number of characters added
    """
    with open(filename, "a") as f:
        n_append = f.write(text)

        return (n_append)
