#!/usr/bin/python3
"""First Rectangle"""
Base = __import__('base').Base


class Rectangle(Base):
    """Represent a rectangle"""
    __width
    __height
    __x
    _y

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle
        Args:
        width: width of rectangle      
        height: height of rectangle
        x: x-position of rectangle
        y:y-position of rectangle
        id: ID of rectangle
        """
        super(id)
        width = width
        height = height
        x = x
        y = y

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

    @width.setter
    def width(self, width):
        """Set the width of rectangle
        Args:
        width: width of rectangle
        """
        self.__width = width

    @height.setter
    def height(self, height):
        """Set the height of rectangle
        Args:
        height: height of rectangle
        """
        self.__height = height

    @x.setter
    def x(self, x):
        """Set the x position of rectangle
        Args:
        x: x position of rectangle
        """
        self.__x = x

    @width.setter
    def width(self, width):
        """Set the width of rectangle
        Args:
        width: width of rectangle
        """
        self.__width = width
