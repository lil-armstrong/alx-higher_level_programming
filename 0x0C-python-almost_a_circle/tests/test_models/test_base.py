#!/usr/bin/python3
"""Define unittest for models.base"""

import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInit (unittest.TestCase):
    """Unittest for testing Base class initialization"""

    def test_has_docs(self):
        """Everything is documented in models.base"""
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


class TestBaseToJSONString(unittest.TestCase):
    """Unit test to Base.to_json_string"""

    def test_has_method(self):
        """Base has a public method called to_json_stringS"""
        self.assertIn("to_json_string", Base.__dict__)

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        sq = Square(10, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))


class TestBaseSaveToFile(unittest.TestCase):
    """Unittest for Base.save_to_file"""

    def test_has_method(self):
        """Base has a public method called save_to_file"""
        self.assertIn("save_to_file", Base.__dict__)

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        file_paths = ["Rectangle.json",
                      "Square.json",
                      "Base.json"]
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_create_new_file(self):
        """ Create a new file or overwrite existing """
        list_objs = None
        file_path = "Rectangle.json"
        Rectangle.save_to_file(list_objs)
        self.assertTrue(os.path.exists(file_path))

    def test_parse_file(self):
        list_objs = None
        expected_list = []
        file_path = "Rectangle.json"
        Rectangle.save_to_file(list_objs)
        with open(file_path, "r") as f:
            self.assertEqual(expected_list, json.load(f))

    def test_save_to_file_one_rectangle(self):
        file_path = "Rectangle.json"
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])

        with open(file_path, "r") as f:
            data = Rectangle.from_json_string(f.read())
            self.assertDictEqual(data, r.to_dictionary())

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        obj_list = [r1, r2]
        dict = Rectangle.to_json_string(
            [obj.to_dictionary() for obj in obj_list])
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            r = (f.read())
            # dict is an array, whereas the json data is not
            # Make up for the following chars ('[',']', ',', ' ')
            self.assertEqual(len(dict), len(r) + 4)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        dict = s.to_json_string(s.to_dictionary())
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(len(dict), len(f.read()))

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        obj_list = [s1, s2]
        dict = Square.to_json_string([obj.to_dictionary() for obj in obj_list])
        Square.save_to_file(obj_list)
        with open("Square.json", "r") as f:
            r = (f.read())
            # dict is an array, whereas the json data is not
            # Make up for the following chars ('[',']', ',', ' ')
            self.assertEqual(len(r) + 4, len(dict))

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        s.save_to_file([s])
        dict = s.to_json_string(s.to_dictionary())
        with open("Square.json", "r") as f:
            r = f.read()
            self.assertEqual(len(dict), len(r))

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])

        with open("Square.json", "r") as f:
            r = Square.from_json_string(f.read())
            self.assertDictEqual(s.to_dictionary(), r)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        Square.save_to_file()
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
