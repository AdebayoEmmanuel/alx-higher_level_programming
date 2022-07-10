#!/usr/bin/python3
"""This class inherits list
    and has a method that returns
    the sorted list
"""


class MyList(list):
    """This class inherits list"""

    def print_sorted(self):
        """prints the list sorted"""
        print(sorted(self))
