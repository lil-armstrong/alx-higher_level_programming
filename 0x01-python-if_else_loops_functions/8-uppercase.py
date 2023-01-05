#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print(f"{chr(ord(c) - 32)}", end="")
        else:
            print(f"{c}", end="")
        print("")
