#!/usr/bin/python3
"""This module contains one square class
    with private instance attribute 'size'
    type and value control is introduced
    now
"""


class Square:
    """A square class with size attribute"""

    def __init__(self, size=0):
        """Instantiation method for square object
            with a private size attribute
        """
        self.size = size

    @property
    def size(self):
        """Getter property for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter property for size with controls"""
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
