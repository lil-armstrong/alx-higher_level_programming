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


class TestSquareUpdate(unittest.TestCase):
    """Unitest for update method in Square"""

    def test_has_method(self):
        """Square has a public method called update"""
        self.assertIn("update", Square.__dict__)

    def test_update_args(self):
        square = Square(3, 5)
        square.update(10, 4, 2, 0)

        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_update_kwargs(self):
        square = Square(3, 5)
        square.update(size=10, id=4, x=2, y=1)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)


class TestRectangleToDicttest(unittest.TestCase):
    """Unitest for to_dictionary method in Square"""

    def test_has_method(self):
        """Square has a public method called to_dictionary"""
        self.assertIn("to_dictionary", Square.__dict__)

    def test_return_value(self):
        """Test return value of to_dictionary"""
        self.assertDictEqual(Square(4, 2, id=4).to_dictionary(), {
            "id": 4,
            "size": 4,
            "x": 2,
            "y": 0
        })
