#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """A function that replaces an element of a list at a specific position

    Args:
        my_list: list object containing integers
        idx: the index of the element to be replaced
        element: element to be inserted

    Returns: Original list if idx is negative or out of range, otherwise
            returns modified list with element at index idx replaced

    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
