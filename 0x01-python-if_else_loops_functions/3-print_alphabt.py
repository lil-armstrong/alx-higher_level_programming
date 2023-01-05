#!/usr/bin/python3
"""Prints alphabets in lowercase."""
for i in range(97, 122):
    if chr(i) not in 'qe':
        print(f"{chr(i)}", end="")
