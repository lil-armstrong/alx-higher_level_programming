#!/usr/bin/python3
def magic_string():
    magic_string.cnt = getattr(magic_string, 'cnt', 0) + 1
    return str.join(", ", ["BestSchool" for i in range(magic_string.cnt)])
