#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file after each line\
    containing a specific string

    Args:
    filename(str): File name path
    search_string(str): String to search for in each line
    new_string(str): New string to append

    """
    with open(filename, "r+", encoding="utf-8") as fp:
        fp.seek(0, 0)
        text = ""
        # for line in fp:
        line = fp.readline()
        while line:
            text += line
            if search_string in line:
                text += new_string
            line = fp.readline()
        fp.seek(0, 0)
        fp.write(text)
