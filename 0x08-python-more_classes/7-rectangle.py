#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""

    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Class initializer"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter"""
        return (0 if (self.width == 0 or self.height == 0)
                else 2 * (self.width + self.height))

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

    def __repr__(self):
        """Return a eval compliant string representation of instance."""
        return ("Rectangle("
                + str(self.width)
                + ", "
                + str(self.height)
                + ")"
                )

    def __del__(self):
        """Detect instance deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
