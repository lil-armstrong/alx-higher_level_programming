#!/usr/bin/python3
"""Geometry modile"""


class BaseGeometry:
    """Represent a Geometry object."""

    def area(self):
        """Calculate the area of the geomtry"""
        raise Exception("area() is not implemented")
