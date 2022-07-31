#!/usr/bin/env python3
"""This module has a function that reads text file"""


def read_file(filename=""):
    """This function reads a text file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
