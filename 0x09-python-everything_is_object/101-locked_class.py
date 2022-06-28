#!/usr/bin/python3
"""Defines a class that can only be instantiated with first name"""


class LockedClass:
    """Locked class with one permissible attribute"""

    __slots__ = ["first_name"]
