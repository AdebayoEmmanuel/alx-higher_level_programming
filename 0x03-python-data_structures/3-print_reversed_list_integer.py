#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """This funciton prints the element of list in reverse

        Args:
            my_list: the list to be printed

        Return: None
    """
    for i in reversed(my_list):
        print("{:d}".format(i))
