#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function that replaces an element of a list at a specific position
        without modifying thew original list

    Args:
        my_list: list object containing integers
        idx: the index of the element to be replaced
        element: element to be inserted

    Returns: Original list if idx is negative or out of range, otherwise
            returns (copied) modified list with element at index idx replaced

    """
    new_list = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return new_list
