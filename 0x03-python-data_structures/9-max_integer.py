#!/usr/bin/python3
def max_integer(my_list=[]):
    """A function that returns the max integer in a list
        
        Args:
        my_list: A list of integers

        Returns:
        None if list is empty, otherwise, returns max integer in list
    """
    sorted_list = sorted(my_list, reverse = True)
    if len(my_list) == 0:
        return None
    return sorted_list[0]
    
