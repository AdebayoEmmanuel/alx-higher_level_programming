#!usr/bin/python3
"""This module contains a function which divides a matrix."""


def matrix_divided(matrix, div):

    """A function that divides a matrix.
    Args:
       matrix: a list of lists of int or float type.
       div: thee divisor of int or float type.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        a new matrix which is the original matrix but with the
        elements divided by div, rounded to 2 decimal places.
    """

    if type(div) not in [int, float] or div == float('nan'):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not (isinstance(matrix, list)) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    else:
        for item in matrix:
            if not (isinstance(item, list)) or item == []:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            else:
                for j in item:
                    if not (isinstance(j, (int, float))):
                        raise TypeError("matrix must be a matrix (list of"
                                        " lists) of integers/floats")
    length = len(matrix[0])

    for item in matrix:
        if not (len(item) == length):
            raise TypeError("Each row of the matrix must have the same size")

    result = [[round((num/div), 2) for num in item] for item in matrix]

    return result
