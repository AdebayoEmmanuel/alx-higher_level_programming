#!/usr/bin/python3
"""This is our base class
    other classes to be
    modeled after this one
"""
import json
import csv
import turtle


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
            for obj in list_objs:
                jsonlist.append(obj.to_dictionary())

        storage = cls.to_json_string(jsonlist)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(storage)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if not json_string or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that creates instances and returns its dict"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads instances from a file"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as myfile:
                read = myfile.read()
                dictionary_string = cls.from_json_string(read)
                instance_list = []
                for dictionary in dictionary_string:
                    instance_list.append(cls.create(**dictionary))
                return instance_list
            except IOError:
                return []
