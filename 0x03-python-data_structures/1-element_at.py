#!/usr/bin/python3
def element_at(my_list, idx):
    """A function that retrieves an element from a list

    Args:
        my_list: list of integers
        idx: the index of the element to be retrieved
    
    Returns: None if idx is negative or out of range, otherwise returns 
             element at index idx

    """
    if idx < 0 or idx >= len(my_list):
        return (None)
    return (my_list[idx])
