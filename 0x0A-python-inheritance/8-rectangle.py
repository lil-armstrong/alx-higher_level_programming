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
