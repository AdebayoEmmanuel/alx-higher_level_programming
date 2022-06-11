#!/usr/bin/python3
def islower(c):
    """A function that tests if a character is lower case or not

       Args:
       c: the character to check against

       Return:
       True if c is lowercase, False otherwise
    """
    if ord(c) in range(97, 123):
        return True
    else:
        return False
