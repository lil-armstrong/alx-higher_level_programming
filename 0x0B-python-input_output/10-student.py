#!/usr/bin/python3

"""Student to JSON with filter"""


class Student:
    """Represents a student as a class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student class.

        Args:
        first_name: First name of student
        last_name: Last name of student
        age: Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve all/some dictionary representation of a student instance.

        Args:
        attrs: (list)Attributes to filter and show

        Returns:
        The dictionary representation of an instance of Student based on attrs
        """
        if (type(attrs) in [list]):
            return {x: y for (x, y) in self.__dict__.items() if x in attrs}
        return self.__dict__
