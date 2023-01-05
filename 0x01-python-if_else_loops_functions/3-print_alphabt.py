#!/usr/bin/python3
"""Prints alphabets in lowercase."""
for i in range(97, 123):
    if chr(i) not in 'qe':
        print("{}".format(chr(i)), end="")
