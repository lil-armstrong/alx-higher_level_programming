#!/usr/bin/python3

"""My integer"""


class MyInt(int):
    """Rebel integer derived class."""

    def __eq__(self, value):
        """Equality magic method

        Args:
        value (int): Integer value

        Returns:
        Inverse of ==
        """
        return (self.__int__() != value)

    def __ne__(self, value):
        """Not equal magic methid override

        Args:
        value (int): Integer value

        Returns:
        Inverse of !=
        """
        return (self.__int__() == value)
