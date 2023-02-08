#!/usr/bin/python3

"""Pascal triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the\
    the pascal's triangle of n

    Args:
    n (int): max level of triangle to generate

    Returns:
    List of lists of integers
    """
    if n <= 0:
        return []
    res = []

    for i in range(n):
        temp = []
        prev = None if (len(res) == 0) else (len(res) - 1)
        if (prev is None):
            temp = [1]
        else:
            for x in range(len(res[prev]) + 1):
                if x > 0 and x < len(res[prev]):
                    temp.append(res[prev][x] + res[prev][x-1])
                else:
                    temp.append(1)
        res.append(temp)
    return res
