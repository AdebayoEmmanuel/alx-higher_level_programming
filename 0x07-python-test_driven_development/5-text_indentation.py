#!/usr/bin/python3
"""This module defines a function that indents a string"""


def text_indentation(text):
    """This function formating text.
    Return the result in new text.
    Raise Error if data is diferrent."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    check = False
    for i in range(len(text)):
        if text[i] in [".", ":", "?"]:
            print(text[x : i + 1])
            print()
            x = i + 2
            bool = True
    if i + 1 == len(text) and bool is False:
        print(text)
