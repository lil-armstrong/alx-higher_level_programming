#!/usr/bin/python3
"""And now, the Square!"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rerpresent a Square"""
    __size = 0

    def __init__(self, size, x=0, y=0, id=None):
        """Initilize the rectang;e instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square instance"""
        self.isInt("width", value)
        self.isNonZeroPositive("width", value)
        self.__size = value

    def __str__(self):
        """Return rectangle description"""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id,
                                              self.x,
                                              self.y,
                                              self.height))

    def update(self, *args, **kwargs):
        """Assign an argument to each ttribute"""
        if (args and len(args)):
            for id, arg in enumerate(args):
                if (id == 0):
                    self.id = arg
                if (id == 1):
                    self.size = arg
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
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
