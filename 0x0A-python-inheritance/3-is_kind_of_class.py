#!/usr/bin/python3
"""This module checks whether or not
    an obj is an instance oc a class
    or an instance of a class inherited
    from it
"""


def is_kind_of_class(obj, a_class):
    """This function checks whether an object
        is an instance of a class or not
    """

    return isinstance(obj, a_class)
