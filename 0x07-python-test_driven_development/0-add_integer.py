#!/usr/bin/python3
"""
    TDD rules
"""
def add_integer(a, b=98):
    """
        This function sums two integers a and b

        Args:
            a - int or float input (floats must be first casted to int)
            b - int or float input, defaults to 98

        Return:
            integer sum of a and b
            or TypeError exception if a and b are not ints
    """
    if not (isinstance(a, (float, int))):
        raise TypeError('a must be an integer')
    if not (isinstance(b, (float, int))):
        raise TypeError('b must be an integer')
    if isinstance(a, (float, int)) or isinstance(b, (float, int)):
        a = int(a)
        b = int(b)
    return int(a + b)
