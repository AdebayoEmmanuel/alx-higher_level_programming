#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """A function that prints integers

    Args:
        my_list: list of integers to be printed

    Returns: None

    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
