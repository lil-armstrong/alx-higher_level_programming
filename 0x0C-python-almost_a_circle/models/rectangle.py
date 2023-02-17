#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    __width = 0
    __height = 0
    __x = 0
    _y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle
        Args:
        width: width of rectangle      
        height: height of rectangle
        x: x-position of rectangle
        y:y-position of rectangle
        id: ID of rectangle
        """
        super().__init__(id=id)

        self.height = height
        self.width = width
        self.y = y
        self.x = x

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @property
    def x(self):
        """Get x positon of rectangle"""
        return self.__x

    @property
    def y(self):
        """Get y position of rectangle"""
        return self.__y

    def isInt(self, name, value):
        """Check if value is an integer

        Args:
        name: name of attribute
        value: value of attribute
        """
        if (not isinstance(value, (int))):
            raise TypeError("{} must be an integer".format(name))

    def isNonZeroPositive(self, name, value):
        """Validate positivity of an attribute value

        Args:
        name: name of attribute
        value: value of attribute
        """
        if not (value > 0):
            raise ValueError("{} must be > 0".format(name))

    def isPositive(self, name, value):
        """Validate positivity of an attribute value

        Args:
        name: name of attribute
        value: value of attribute
        """
        if not (value >= 0):
            raise ValueError("{} must be >= 0".format(name))

    @width.setter
    def width(self, width):
        """Set the width of rectangle
        Args:
        width: width of rectangle
        """
        self.isInt("width", width)
        self.isNonZeroPositive("width", width)
        self.__width = width

    @height.setter
    def height(self, height):
        """Set the height of rectangle
        Args:
        height: height of rectangle
        """
        self.isInt("height", height)
        self.isNonZeroPositive("height", height)
        self.__height = height

    @x.setter
    def x(self, x):
        """Set the x position of rectangle
        Args:
        x: x position of rectangle
        """
        self.isInt("x", x)
        self.isPositive("x", x)
        self.__x = x

    @y.setter
    def y(self, y):
        """Set the y position of rectangle
        Args:
        y: y position of rectangle
        """
        self.isInt("y", y)
        self.isPositive("y", y)
        self.__y = y

    def area(self):
        """Get the area of rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Print to stdout the Rectangle instance with the character #"""
        if (self.width == 0 or self.height == 0):
            return ""
        content = ""
        content += "".join(["\n" for y in range(self.y)])

        for h in range(self.height):
            content += "".join([" " for x in range(self.x)])
            for w in range(self.width):
                content += "#"
            content += "\n" if (h < self.height - 1) else ""
        print(content)

    def __str__(self):
        """Return rectangle description"""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width,
                                                 self.height))

    def update(self, *args, **kwargs):
        """Assign an argument to each ttribute"""
        if (args and len(args)):
            for id, arg in enumerate(args):
                if (id == 0):
                    self.id = arg
                if (id == 1):
                    self.width = arg
                if (id == 2):
                    self.height = arg
                if (id == 3):
                    self.x = arg
                if (id == 4):
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if (key == 'id'):
                    self.id = value
                if (key == 'width'):
                    self.width = value
                if (key == 'height'):
                    self.height = value
                if (key == 'x'):
                    self.x = value
                if (key == 'y'):
                    self.y = value

    def to_dictionary(self):
        """Get the dictionary representation of a Rectangle instance"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
