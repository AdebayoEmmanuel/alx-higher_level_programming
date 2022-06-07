#!/usr/bin/python3
def no_c(my_string):
    """A function that removes all character c and C from a string

    Args:
        my_string: string to be modified

    Returns: Modified string

    """
    result = ''
    for i in range(len(my_string)):
        if my_string[i].lower() != 'c':
            result += my_string[i]
    return result
