#!/usr/bin/python3
"""This module appends to file end"""


def write_file(filename="", text=""):
    """Takes a file and a text, append text to file
        returns number of characters added
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
