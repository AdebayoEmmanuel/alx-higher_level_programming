#!/usr/bin/python3
"""This module contains one function
    that returns a list of available
    attributes and methods of an object
"""


def lookup(obj):
    """This function returns a list of all
        attributes and methods of an object

        Args:
            obj - the object to be passed
        Returns:
            A list object of all attributes
            and methods
    """
    return dir(obj)
