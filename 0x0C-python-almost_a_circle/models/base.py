#!/usr/bin/python3
"""This is our base class
    other classes to be
    modeled after this one
"""


class Base:
    """this class has some weird
        init rules, you'll see
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """weird init, called it"""
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
