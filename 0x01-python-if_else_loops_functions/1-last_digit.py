#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
report = ""
sym = '-' if number < 0 else ""
last_digit = sym + last_digit

if int(last_digit == 0):
    report = "is 0"
if int(last_digit) < 6:
    report = "is less than 6 and not 0"
elif int(last_digit) > 5:
    report = "is greater than 5"

print(f"Last digit of {number} is {last_digit} and {report}")
