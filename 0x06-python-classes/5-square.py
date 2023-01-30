#!/usr/bin/python3

"""Define a class: Square."""


class Square:
    """Represent a square class."""

    def __init__(self, size=0):
        """Class initializer."""
        self.size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size property."""
        return self.__size

    @size.setter
    def size(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def my_print(self):
        """Print the square with the # character."""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
