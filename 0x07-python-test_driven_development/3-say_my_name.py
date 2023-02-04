#!/usr/bin/python3
"""Print a string in the format ``My name is <first name> <last name>.``"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

    Args:
    first_name: string
    last_name: string. Default is empty string

    Raises:
    TypeError: if either first_name and last_name is not a string
    """
    if (not isinstance(first_name, (str))):
        raise TypeError("first_name must be a string")

    if (not isinstance(last_name, (str))):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(
        first_name, last_name))
