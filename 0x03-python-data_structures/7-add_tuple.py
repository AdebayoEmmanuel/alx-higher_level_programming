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

    # This block groups the respective elements as tuples
    tup_elem = ()
    for a, b in zip(tuple_a, tuple_b):
        tup_elem += ((a, b),)

    # sums the respective first and second elements
    sum_first = tup_elem[0][0] + tup_elem[0][1]
    sum_sec = tup_elem[1][0] + tup_elem[1][1]
    return_tuple = (sum_first, sum_sec)

    return (return_tuple)
