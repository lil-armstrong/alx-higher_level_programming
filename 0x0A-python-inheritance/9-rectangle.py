#!/usr/bin/python3
"""Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectange using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle instance.

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return rectangle description"""
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
