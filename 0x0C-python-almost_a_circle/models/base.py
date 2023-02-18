#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Represent the base of other classes in this project."""
    __nb_objects = 0
    # __uid = []

    def __init__(self, id=None):
        """Manage id attribute to avoid duplication"""
        Base.__nb_objects += 1
        if not (id is None):
            self.id = id
        else:
            self.id = Base.__nb_objects
        # while (self.id in self.__uid):
        #     self.id += 1

        # self.__uid.append(id)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Get the JSON string representaion of list_dictionaries

        Args:
        list_dictionaries: dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Get the JSON string representaion of json_string

        Args:
        json_string: json string representing list of dictionaries
        """
        if json_string is None:
            return []
        return [json.loads(json_string)]

    @classmethod
    def create(cls, **dictionary):
        """Create an instanc with all the attributes set

        Args:
        dictionary: doctionary of attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def save_to_file(cls, list_objs=None):
        """Write the JSON string representaion to a file

        Args:
        list_objs: List of instances that inherit fro Base
        """
        file = "{}.json".format(cls.__name__)
        with open(file, "w") as fp:
            if (list_objs is None) or (len(list_objs) == 0):
                fp.write("[]")
            else:
                for obj in list_objs:
                    if (isinstance(obj, Base)):
                        obj_dict = Base.to_json_string(obj.to_dictionary())
                        fp.write(obj_dict)

    @classmethod
    def load_from_file(cls):
        """Return a list of instancs"""
        file = "{}.json".format(cls.__class__.__name__)
        try:
            with open(file, 'r') as fp:
                dict_list = cls.from_json_string(fp.read())
                return [cls.create(**d) for dict in dict_list]
        except IOError:
            return []
