#!/usr/bin/python3
import random
number = random.randint(-10, 10)
str = "is zero"
"""Check if a random number is either zero, positive or negative."""
if number < 0:
    str = "is negative"
elif number > 0:
    str = "is positive"
else:
    str = "is zero"
print(f"{number} {str}")
