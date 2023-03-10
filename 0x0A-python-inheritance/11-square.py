#!/usr/bin/python3
"""Square #2"""

Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize Square object"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def __str__(self):
        """Describe square instance"""
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__size,
                                    self.__size))
