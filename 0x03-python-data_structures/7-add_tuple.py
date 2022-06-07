#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """This function adds two tuples

        Args:
            tuple_a: The first tuple argument
            tuple_b: The second tuple argument

        Return: a tuple with two integers
    """

    len_a = len(tuple_a)
    len_b = len(tuple_b)

    # This block checks if the tuple have at least 2 elements
    if len_a < 2:
        if len_a == 1:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, 0)
    elif len_b < 2:
        if len_b == 1:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, 0)
    
    res = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return (res)
