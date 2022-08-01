#!/usr/bin/python3
"""This module generates the dictionary description of an obj"""


def class_to_json(obj):
    """Returns a dictionary representation of a class and all its attributes"""
    return obj.__dict__
