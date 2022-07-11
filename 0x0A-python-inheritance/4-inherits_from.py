#!/usr/bin/python3
"""This module checks whether or not
    an object is an instance of a class
    inherited from another class only
"""


def is_kind_of_class(obj, a_class):
    """This function checks whether an object
        is an instance of a class or not
    """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
