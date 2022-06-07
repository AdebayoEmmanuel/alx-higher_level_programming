#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """This funciton prints the elements of the matrix

        Args:
            matrix: a matrix of integers

        Return: nothing

    """
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="\n")
            else:
                print("{:d}".format(row[i]), end=" ")
