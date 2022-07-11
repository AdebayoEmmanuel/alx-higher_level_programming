#!/usr/bin/python3
"""This rectangle inherits base"""


from models.base import Base


class Rectangle(Base):
    """This class has even weirder init"""

    
    def __init__(self, width, height, x=0, y=0, id=None):
        """okay not that weird, just using Base id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value
