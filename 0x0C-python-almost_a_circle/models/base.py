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
    def to_json_string(dict_list):
        """Get the JSON string representaion of list_dictionaries

        Args:
        list_dictionaries: list of dictionary
        """
        if dict_list is None or len(dict_list) == 0:
            return "[]"
        return json.dumps(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries

        Args:
        json_string: json string representing list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

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
    def save_to_file(cls, dict_list=None):
        """Write the JSON string representaion to a file

        Args:
        list_objs: List of dictionary 
        """
        file = "{}.json".format(cls.__name__)
        with open(file, "w") as fp:
            if (dict_list is None):
                fp.write("[]")
            else:
                obj_dict_list = Base.to_json_string(
                    [obj.to_dictionary() for obj in dict_list if (
                        isinstance(obj, (cls)) and "to_dictionary" in cls.__dict__)]
                )
                fp.write(obj_dict_list)

    @classmethod
    def load_from_file(cls):
        """Return a list of instancs"""
        file = "{}.json".format(cls.__name__)
        try:
            with open(file, 'r') as fp:
                from_file = json.load(fp)
                dict_list = from_file
                return [cls.create(**d) for d in dict_list]
        except IOError:
            return []
