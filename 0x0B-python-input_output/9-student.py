#!/usr/bin/python3
"""This module creates a class anbd has a method to return
    its dictionary representation with all attributes.
"""


class Student:
    """Student class to get dict from"""
    
    def __init__(self, first_name, last_name, age):
        """Constructor for studenty object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This is where the dictionary thing happens"""

        return self.__dict__
