#!/usr/bin/python3
def multiple_returns(sentence):
    """A function that returns a tuple
        with the length of a string and its first char

        Args:
        sentence: the string to be used

        Returns:
        a tuple containing the first character and sentence length
        if len(sentence) is empty, the first char equals None
    """
    length = len(sentence)
    first = sentence[0]
    if length == 0:
        first = None
    res = (length, first)
    return res
