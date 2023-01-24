#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide two integers and print the result.

    Args
        a: The first integer.
        b: The second integer.

    Returns
        result pf division or None
    """

    try:
        result = a/b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
