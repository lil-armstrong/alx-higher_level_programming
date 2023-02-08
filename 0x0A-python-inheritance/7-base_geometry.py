#!/usr/bin/python3
"""Geometry modile"""


class BaseGeometry:
    """Represent a Geometry object."""

    def area(self):
        """Calculate the area of the geomtry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer values."""
        if (not isinstance(value, (int))):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
