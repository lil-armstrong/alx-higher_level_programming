#!/usr/bin/python3

"""Define a class: Square."""


class Square:
    """Represent a square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Class initializer."""
        self.size = size
        self.position = position

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
            [print("") for j in range(self.position[1])]
            for i in range(self.size):
                [print(" ", end="") for j in range(self.position[0])]
                [print("#", end="") for k in range(self.size)]
                print("")

    @property
    def position(self):
        """Return position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position value."""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(el >= 0 for el in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
