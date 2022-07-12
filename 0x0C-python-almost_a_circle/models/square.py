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

    def update(self, *args, **kwargs):
        """this method updates square with
            variable positional and keyword
            arguments
        """

        for i in len(args):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.size = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]

        if not args or if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
