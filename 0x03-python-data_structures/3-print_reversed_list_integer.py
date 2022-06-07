#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints integers in reverse from a list

    Args:
        my_list: list of integers to be printed

    Returns: None

    """
    i = (len(my_list) - 1)
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
