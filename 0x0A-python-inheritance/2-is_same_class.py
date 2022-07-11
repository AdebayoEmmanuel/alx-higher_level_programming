#!/usr/bin/python3
"""This module checks whether or not
    an obj is an instance oc a class
"""


def is_same_class(obj, a_class):
    """This function checks whether an object
        is an instance of a class or not
    """

    return type(obj) == a_class
