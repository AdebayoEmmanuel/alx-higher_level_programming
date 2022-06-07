#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """This funciton prints the element of list in reverse

        Args:
            my_list: the list to be printed

        Return: None
    """
    last_idx = len(my_list) - 1
    for i in range(last_idx, -1, -1):
        print("{:d}".format(my_list[i]))
