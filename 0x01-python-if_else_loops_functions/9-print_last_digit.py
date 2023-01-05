#!/usr/bin/python3

def print_last_digit(number):
    """Print the last digit of a number."""
    if isinstance(number, int):
        print(str(number)[-1], end="")
    else:
        raise TypeError("NaN")
    return str(number)[-1]
