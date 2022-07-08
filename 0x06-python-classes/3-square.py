#!/usr/bin/python3
"""This module contains one square class
    with private instance attribute 'size'
    with type and value control
    And a public attribute area
"""


class Square:
    """A square class with size attribute"""

    def __init__(self, size=0):
        """Instantiation method for square object
            with a private size attribute
        """
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of a square,
            based on its given size
        """
        return (self.__size ** 2)
