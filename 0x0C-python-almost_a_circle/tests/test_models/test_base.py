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

    def test_file_path(self):
        """ Create a new file or overwrite existing """
        list_objs = None
        file_path = "Base.json"
        Base.save_to_file(list_objs)
        self.assertTrue(os.path.exists(file_path))
        if os.path.exists(file_path):
            os.remove(file_path)

        file_path = "Rectangle.json"
        Rectangle.save_to_file(list_objs)
        self.assertTrue(os.path.exists(file_path))
        if os.path.exists(file_path):
            os.remove(file_path)

        file_path = "Square.json"
        Square.save_to_file(list_objs)
        self.assertTrue(os.path.exists(file_path))
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

    def test_load_from_filel(self):
        """ Load object instances from json file """
        file_path = "Rectangle.json"
        expected = [Rectangle(10, 7, 2, 8, 5)]

        Rectangle.save_to_file(expected)
        from_file = Rectangle.load_from_file()
        self.assertIsInstance(from_file, list)
        self.assertTrue(
            all([
                isinstance(item, (Rectangle, Base))
                for item in from_file
            ])
        )

    def test_save_single_rectangle(self):
        file_path = "Rectangle.json"
        expected = [Rectangle(10, 7, 2, 8, 5)]

        Rectangle.save_to_file(expected)
        from_file = Rectangle.load_from_file()
        self.assertEqual(len(expected), len(from_file))
        for index, res in enumerate(expected):
            self.assertEqual(res.to_dictionary(),
                             from_file[index].to_dictionary())

    def test_save_multiple_rectangles(self):
        file_path = "Rectangle.json"
        expected = [
            Rectangle(10, 7, 2, 8, 5),
            Rectangle(8, 1, 2, 3)
        ]

        Rectangle.save_to_file(expected)
        from_file = Rectangle.load_from_file()
        for index, res in enumerate(expected):
            self.assertEqual(res.to_dictionary(),
                             from_file[index].to_dictionary())

    def test_save_square(self):
        file_path = "Square.json"
        s = Square(10, 7, 2, 8)
        expected = [s]

        Square.save_to_file(expected)
        from_file = Square.load_from_file()
        for index, res in enumerate(expected):
            self.assertEqual(res.to_dictionary(),
                             from_file[index].to_dictionary())

        # =============MULTIPLE=================
        expected = [Square(10, 7, 2, 8), Square(8, 1, 2, 3)]

        Square.save_to_file(expected)
        with open(file_path, "r") as f:
            from_file = json.load(f)
            self.assertEqual(len(from_file), len(expected))
            for index, res in enumerate(expected):
                self.assertEqual(res.to_dictionary(), from_file[index])

    def test_save_to_file_cls_name_for_filename(self):
        file_path = "Square.json"
        expected = [Square(10, 7, 2, 8)]

        Square.save_to_file(expected)
        with open(file_path, "r") as f:
            from_file = json.load(f)
            self.assertEqual(len(expected), len(from_file))
            for index, res in enumerate(expected):
                self.assertEqual(res.to_dictionary(), from_file[index])

    def test_save_to_file_overwrite(self):
        file_path = "Square.json"
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        expected = [s]

        Square.save_to_file(expected)
        with open(file_path, "r") as f:
            from_file = json.load(f)
            self.assertEqual(len(expected), len(from_file))
            for index, res in enumerate(expected):
                self.assertEqual(res.to_dictionary(), from_file[index])

    def test_save_to_file_None(self):
        file_path = "Square.json"
        Square.save_to_file(None)
        with open(file_path, "r") as f:
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
