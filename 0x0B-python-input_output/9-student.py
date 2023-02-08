#!/usr/bin/python3
"""Student to JSON"""


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

    def to_json(self):
        """Retrieve dictionary representation of a student instance."""
        return self.__dict__
