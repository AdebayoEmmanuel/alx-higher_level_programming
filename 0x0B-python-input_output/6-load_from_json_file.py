#!/usr/bin/python3
"""This module creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """CREATES PYTHON object from JSON file"""
    with open(filename) as myFile:
        return json.load(myFile)
