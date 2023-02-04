#!/usr/bin/python3
"""Divide all elements of a matrix by a divisor"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
    matrix: list of lists of integers or floats
    div: divisor

    Raises:
    ZeroDivisionError: if the value of div is zero
    TypeError: if matrix is not a list of lists of integers/floats
    TypeError: if each row of the matrix are not the same size
    TypeError: if ``div`` is not a number
    """
    if (not isinstance(matrix, list)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    else:
        is_list = all([isinstance(x, list) for x in matrix])
        if (not is_list or
                not all([isinstance(i, (int, float))
                         for j in matrix for i in j])):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        else:
            ref_size = len(matrix[0])
            for i in range(1, len(matrix)):
                if (ref_size != len(matrix[i])):
                    raise TypeError(
                        "Each row of the matrix must have the same size")

            if (not isinstance(div, (int, float))):
                raise TypeError("div must be a number")

            if (div == 0):
                raise ZeroDivisionError("division by zero")

            # for i, j in enumerate(matrix):
            #     result.append([])
            #     for k in j:
            #         result[i].append(round(k/div, 2))
            return [
                [round(k/div, 2) for k in j]
                for i, j in enumerate(matrix)
            ]
