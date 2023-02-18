#!/usr/bin/python3

"""Define unittest for models.rectangle"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleInit(unittest.TestCase):
    """unittest suite for rectangle class"""

    def test_has_docs(self):
        """Everything is documented in models.rectangle"""
        self.assertTrue(len(Rectangle.__doc__) > 10)

    def test_call_super_with_id(self):
        """Call super class with ID"""
        b = Base()
        r1 = Rectangle(10, 70, 0, 0)
        self.assertEqual(r1.id, b.id + 1)
        r1 = Rectangle(10, 70, 0, 0, 35)
        # r1 = Rectangle(30, 23)
        # r1 = Rectangle(16, 60)
        self.assertEqual(r1.id, 35)

    def test_is_subclass_of_base(self):
        """Rectangle inherits from Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_width_mutator_accessor(self):
        """Private attribute, width has a setter"""
        rect = Rectangle(20, 30)
        self.assertEqual(rect.width, 20)
        rect.width = 40
        self.assertEqual(rect.width, 40)

    def test_height_mutator_accessor(self):
        """Private attribute, height has a setter"""
        rect = Rectangle(20, 30)
        self.assertEqual(rect.height, 30)
        rect.height = 40
        self.assertEqual(rect.height, 40)

    def test_x_mutator_accessor(self):
        """Private attribute, x has a setter"""
        rect = Rectangle(20, 30)
        self.assertEqual(rect.x, 0)
        rect.x = 40
        self.assertEqual(rect.x, 40)

    def test_y_mutator_accessor(self):
        """Private attribute, y has a setter"""
        rect = Rectangle(20, 30)
        self.assertEqual(rect.y, 0)
        rect.y = 40
        self.assertEqual(rect.y, 40)

    def test_can_create_with_width_and_height(self):
        """Can create an instance of Rectangle with width and height"""
        rect = Rectangle(20, 30)
        self.assertIsInstance(
            rect, Rectangle, "Cannot create a rectangle with width and height")

    def test_has_display_method(self):
        """Rectangle has a public method called display"""
        self.assertIn("display", Rectangle.__dict__)


class TestRectangleArea(unittest.TestCase):
    """Unitest for area method in Rectangle"""

    def test_has_area_method(self):
        """Rectangle has a public method called area"""
        self.assertIn("area", Rectangle.__dict__)

    def test_area(self):
        rect = Rectangle(3, 5)
        self.assertEqual(rect.area(), 3 * 5)


class TestRectangle__Str_(unittest.TestCase):
    """Unitest for area method in Rectangle"""

    def test___str__(self):
        rect = Rectangle(3, 5)
        self.assertEqual(str(rect),
                         "[{}] ({}) {}/{} - {}/{}".
                         format(rect.__class__.__name__,
                                rect.id,
                                0,
                                0,
                                3,
                                5))


class TestRectangleIntValidator(unittest.TestCase):
    """Unitest for attribute validation in Rectangle"""

    def test_width_NaN(self):
        with self.assertRaises((TypeError,)):
            rect = Rectangle("0", 5)

    def test_height_NaN(self):
        with self.assertRaises((TypeError,)):
            rect = Rectangle(5, "56")

    def test_width_gt_zero(self):
        with self.assertRaises((ValueError,)):
            rect = Rectangle(0, 5)
        with self.assertRaises((ValueError,)):
            rect = Rectangle(-3, 5)

    def test_height_gt_zero(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            rect = Rectangle(15, -3, 5)

    def test_x_lt_zero(self):
        with self.assertRaises((ValueError,)):
            rect = Rectangle(7, 5, -13)

    def test_y_lt_zero(self):
        with self.assertRaises((ValueError,)):
            rect = Rectangle(7, 5, 74, -13)


class TestRectangleUpdate(unittest.TestCase):
    """Unitest for update method in Rectangle"""

    def test_has_method(self):
        """Rectangle has a public method called update"""
        self.assertIn("update", Rectangle.__dict__)

    def test_update_args(self):
        rect = Rectangle(3, 5)
        rect.update(10, 4, 2, 0, 1)

        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 1)

    def test_update_kwargs(self):
        rect = Rectangle(3, 5)
        rect.update(width=10, id=4, x=2, height=9, y=1)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)


class TestRectangleToDicttest(unittest.TestCase):
    """Unitest for to_dictionary method in Rectangle"""

    def test_has_method(self):
        """Rectangle has a public method called to_dictionary"""
        self.assertIn("to_dictionary", Rectangle.__dict__)

    def test_return_value(self):
        """Test return value of to_dictionary"""
        self.assertDictEqual(Rectangle(4, 2, id=4).to_dictionary(), {
            "id": 4,
            "width": 4,
            "height": 2,
            "x": 0,
            "y": 0
        })
