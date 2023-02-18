#!/usr/bin/python3
"""Define unittest for models.base"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittest suite for Square class"""

    def test_has_docs(self):
        """Everything is documented in models.square"""
        print("\nSquare.__doc__")
        self.assertTrue(len(Square.__doc__) > 10)

    def test_issubclass_of_rectanfle(self):
        """Square is subclass of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))


class TestSquareToDicttest(unittest.TestCase):
    """Unitest for to_dictionary method in Square"""

    def test_has_method(self):
        """Square has a public method called to_dictionary"""
        self.assertIn("to_dictionary", Square.__dict__)

    def test_return_value(self):
        """Test return value of to_dictionary"""
        self.assertDictEqual(Square(4, 1, id=8).to_dictionary(), {
            "id": 8,
            "size": 4,
            "x": 1,
            "y": 0
        })
