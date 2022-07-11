#!/usr/bin/python3
"""This module contains one square class
    with private instance attribute 'size'
    with type and value control for size
    we have getter and setter for size
    and a public area method we are also
    going to print out the square based
    on its size we have included a position
    attribute which must be a tuple of two
    positive integers to specify the coordinate
    where the square will be printed
"""


class Square:
    """A square class with size attribute"""

    def __init__(self, size=0, position=(0,0)):
        """Instantiation method for square object
            with a private size attribute
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter property for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter property for size with controls"""
        if not (type(value) == int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance (position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns the area of a square
            based on the size attribute
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints the square to stdout
            based on the size
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
