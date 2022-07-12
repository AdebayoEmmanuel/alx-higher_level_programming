#!/usr/bin/python3
"""This module contains a
    sqaure class that inherits
    the rectangle class
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A square class that extends our rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize by inheriting rectangle's behaviours"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Getter for square size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size property"""
        self.width = value
        self.height = value

    def __str__(self):
        """str method to overload rectangle's str method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

