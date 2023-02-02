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
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if (not isinstance(value, (int))):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, (int))):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return (0 if (self.width == 0 or self.height == 0)
                else (2 * (self.width + self.height)))

    def __str__(self):
        """Return `string` representation of rectangle"""
        if (self.width == 0 or self.height == 0):
            return ""
        str = ""
        for h in range(self.height):
            for w in range(self.width):
                str += "#"
            str += "\n" if (h < self.height - 1) else ""
        return str
