#!/usr/bin/python3
"""Module multiples two(2) matrices."""


def matrix_mul(m_a, m_b):
    """Multiplies two(2) matrices.

    Args:
    m_a: matrix (list)
    m_b: matrix (list)

    Raises:
    TypeError:
    """
    if (not isinstance(m_a, (list))):
        raise TypeError("m_a must be a list")
    if (not isinstance(m_b, (list))):
        raise TypeError("m_b must be a list")

    def is_not_list_of_lists(matrix=[]): return len(matrix) > 0 and any(
        [not isinstance(x, list) for x in matrix])

    def is_any_empty(matrix=[]): return (len(matrix) == 0 or any(
        [len(x) == 0 for x in matrix]))

    def is_any_nan(matrix=[]): return (len(matrix) > 0 and any(
        [not isinstance(y, (int, float)) for x in matrix for y in x]))

    def is_any_not_same_size(matrix=[]):
        sizes = [len(x) for x in matrix]
        return (len(matrix) > 0
                and
                any([sizes[0] != sizes[y] for y in range(1, len(sizes))]))

    def cannot_multiply(a=[], b=[]):
        a_col = len(a[0])
        b_row = len(b)
        return ((len(a) > 0 and len(b) > 0)
                and
                not (a_col == b_row))

    def matrix_product(a, b):
        result = []
        for i in range(len(a)):
            nrow = []
            for (row_index, a_row) in enumerate(a):
                sum = 0
                for (col_index, b_row) in enumerate(b):
                    sum += b_row[row_index] * a[i][col_index]
                nrow.append(sum)
            result.append(nrow)
        return result

    if (is_not_list_of_lists(m_a)):
        raise TypeError("m_a must be a list of lists")

    if (is_not_list_of_lists(m_b)):
        raise TypeError("m_b must be a list of lists")

    if (is_any_empty(m_a)):
        raise ValueError("m_a can't be empty")
    if (is_any_empty(m_b)):
        raise ValueError("m_b can't be empty")

    if (is_any_nan(m_a)):
        raise TypeError("m_a should contain only integers or floats")
    if (is_any_nan(m_b)):
        raise TypeError("m_b should contain only integers or floats")

    if (is_any_not_same_size(m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if (is_any_not_same_size(m_b)):
        raise TypeError("each row of m_b must be of the same size")

    if (cannot_multiply(m_a, m_b)):
        raise TypeError("m_a and m_b can't be multiplied")

    return matrix_product(m_a, m_b)
