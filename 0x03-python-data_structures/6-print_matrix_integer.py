#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers

    Args:
        matrix: matrix of integers to be printed

    Returns: None

    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
