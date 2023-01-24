#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print an integer.

    Args:
        value: integer value
    """
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
