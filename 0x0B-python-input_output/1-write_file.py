#!/usr/bin/python3
"""This module writes to file"""


def write_file(filename="", text=""):
    """Takes a file and a text, writes text to file
        returns number of texts written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
