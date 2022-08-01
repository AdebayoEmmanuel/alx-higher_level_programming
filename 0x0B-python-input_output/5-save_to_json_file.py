#!/usr/bin/python3
"""this function writes JSON to file."""
import json


def save_to_json_file(my_obj, filename):
    """wrrites python obj to file as JSON str."""
    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
