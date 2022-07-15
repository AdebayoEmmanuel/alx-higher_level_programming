#!/usr/bin/python3
"""This is our base class
    other classes to be
    modeled after this one
"""
import json


class Base:
    """this class has some weird
        init rules, you'll see
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """weird init. called it!"""
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def reset():
        """Resets __nb_objects to 0 to pass test
            cases, since __nb_objct_ value is getting carried
            over from completed tests
        """
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method that returns json encoded
            list of dictionaries

            Args:
                list_dictionaries - a list of dicts

            returns:
                "[]" - if list_dictionaries is None or empty
                JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save JSON to fle"""
        jsonlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for obj in list_obj:
                jsonlist.append(obj.to_dictionary())

        storage = cls.to_json_string(jsonlist)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(storage)
