#!/usr/bin/python3
"""This module contains one square class
    with private instance attribute 'size'
"""


class Square:
    """A square class with size attribute"""

    def __init__(self, size):
        """Instantiation method for square object
            with a private size attribute
        """
        self.__size = size
