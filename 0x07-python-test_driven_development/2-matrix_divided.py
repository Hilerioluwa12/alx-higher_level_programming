#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of lists (integer or float)
        div: int or float for division
    Returns:
        new matrix (int)
    Raises:
        TypeError:
            * matrix must be a matrix (list of lists) of integers/floats
            * Each row of the matrix must have the same size
            * div must be a number
        ZeroDivisionError:
            division by zero
    """
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"
    message3 = "div must be a number"
    message4 = "division by zero"

    if (not matrix) or type(matrix) not in [list]:
        raise TypeError(message1)

    if div == 0:
        raise ZeroDivisionError(message4)

    if len(matrix) == 0:
        raise TypeError(message1)

    if type(div) not in [int, float]:
        raise TypeError(message3)

    for j in matrix:
        if type(matrix) not in [j, list] or len(j) == 0:
            raise TypeError(message1)
        if len(j) != len(matrix[0]):
            raise TypeError(message2)
        for k in j:
            if type(k) not in [int, float]:
                raise TypeError(message1)
    return [[round(k / div, 2) for k in j] for j in matrix]
