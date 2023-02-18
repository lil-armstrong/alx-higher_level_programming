#!/usr/bin/python3
"""Define unittest for models.base"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_initialization (unittest.TestCase):
    """Unittest for testing Base class initialization"""

    def test_has_docs(self):
        """Everything is documented in models.base"""
        print("\nBase.__doc__")
        self.assertTrue(len(Base.__doc__) > 10)

    def test_id(self):
        """Check that given the ID, the next instance increases from the value
        of that ID"""
        base1 = Base()
        base2 = Base(id=1)
        base3 = Base()
        self.assertEqual(base2.id, 1)
        self.assertEqual(base3.id, base1.id + 2)

    def test_private_attribute(self):
        """Check the private attributes of the Base class"""
        instance = Base()
        attrbs = [
            "id"
        ]
        for attrb in attrbs:
            self.assertTrue(attrb in instance.__dict__)

    def test_None_id(self):
        """Check that the ID of the bass class
        increments for every new instance created and if the id is None"""
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance2.id, instance1.id + 1)

    def test_id_is_public(self):
        instance = Base(12)
        instance.id = 20
        self.assertEqual(20, instance.id)

    def test_nb_objects_is_private(self):
        with self.assertRaises(AttributeError):
            Base(12).__nb_objects

    def test_two_argsQ(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unit test to Base.to_json_string"""

    def test_to_json_string_rectangle_type(self):
        print("\nBase.to_json_string")
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        sq = Square(10, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))
