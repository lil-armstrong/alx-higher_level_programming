#!/usr/bin/python3
"""Base class"""


class Base:
    """Represent the base of other classes in this project."""
    __nb_objects = 0

    def __init___(self, id=None):
        """Manage id attribute to avoid duplication"""
        if not (type) in [None]:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
