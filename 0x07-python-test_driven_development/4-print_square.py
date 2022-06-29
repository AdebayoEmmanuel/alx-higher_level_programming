#!/usr/bin/python3
"""This module prints a square"""


def print_square(size):
    """
    This function takes an integer argument
    size and prints a size x size rctangle
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
