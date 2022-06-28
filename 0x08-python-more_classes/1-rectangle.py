#!/usr/bin/python3
class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiotion method for rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width property of a rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of rectangle to value"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves the height property of a rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets height of a rectangle to value"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
