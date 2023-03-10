#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """Class initializer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if (not isinstance(value, (int))):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Return height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, (int))):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter"""
        return (0 if (self.width == 0 or self.height == 0)
                else 2 * (self.width + self.height))
