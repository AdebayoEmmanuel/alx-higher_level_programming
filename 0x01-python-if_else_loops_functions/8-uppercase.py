#!/usr/bin/python3
def uppercase(str):
    """A function that converts a string to uppercase,\
       similar to string.upper()

       Args:
       str: string to be converted

       Return:
       upperStr but in uppercase. i.e STR
    """
    for i in range(len(str)):
        upperStr = str[i]
        if ord(str[i]) in range(97, 123):
            upperStr = chr((ord(str[i]))-32)
        print("{}".format(upperStr), end="")
    print()
