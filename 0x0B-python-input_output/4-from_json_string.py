#!/usr/bin/python3
"""this function returns python object from json."""
import json


def from_json_string(my_str):
    """Decodes normal Python object from JSON."""
    return json.loads(my_str)
