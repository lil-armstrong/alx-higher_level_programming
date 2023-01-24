#!/usr/bin/python3

def safe_print_integer(value):
    """Print an string formatted integer."""
    try:
        print("{:d}".format(value))
    except Exception as exp:
        return False
    else:
        return True
