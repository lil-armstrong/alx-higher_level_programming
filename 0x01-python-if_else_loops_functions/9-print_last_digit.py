#!/usr/bin/python3

def print_last_digit(number):
    """Print the last digit of a number."""
    if type(number) == type(1):
        print(str(number)[-1], end="")
    else:
        raise TypeError("NaN")
    return str(number)[-1]
