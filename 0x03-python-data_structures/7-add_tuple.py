def add_tuple(tuple_a=(), tuple_b=()):
    """This function adds two tuples

        Args:
            tuple_a: first tuple to be added
            tuple_b: second tuple to be added

        Return: a tuple of two ints =, derived by adding tuple_a and tuple:b
    """
    a_len = len(tuple_a)
    b_len = len(tuple_b)

   # if tuples have less than 2 elements, use 0 to replace missing element
    if a_len < 2:
        if a_len == 1:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, 0)
    if b_len < 2:
        if b_len == 1:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, 0)
    res = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return res
