#!/usr/bin/python3
"""Checks if a random number is either zero, positive or negative."""
import random
number = random.randint(-10, 10)
str = "is zero"
if number < 0:
    str = "is negative"
else:
    str = "is positive"
print(f"{number} {str}")
