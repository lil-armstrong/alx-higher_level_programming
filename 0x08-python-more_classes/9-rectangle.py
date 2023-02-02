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
        result = ""
        for h in range(self.height):
            for w in range(self.width):
                result += str(self.print_symbol)
            result += "\n" if (h < self.height - 1) else ""
        return result

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area."""
        if (not isinstance(rect_1, (Rectangle))):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, (Rectangle))):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area = [rect_1.area(), rect_2.area()]
        if (area[0] == area[1]):
            return (rect_1)
        else:
            return (rect_1 if area[0] > area[1] else rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Reactange instance"""
        return Rectangle(size, size)
