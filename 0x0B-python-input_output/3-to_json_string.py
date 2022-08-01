#!/usr/bin/python3
"""this module converts string-to-JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
