#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """A function that finds all multiple of 2 in a list

        Args:
        my_list: the list to fetch multiples from

        Returns:
        my_list, with all multiples of 2 set to True but otherwise set to False
    """
    cpy = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            cpy[i] = True
        else:
            cpy[i] = False
    return cpy
