#!/usr/bin/python3
"""Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectange"""

    def __init__(self, width, height):
        """Initialize rectangle.

        Args:
        width: width of rectangle
        height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return (self.__width * self.__height)

    def print(self):
        """Print"""
        print(self)

    def __str__(self):
        """Return rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
