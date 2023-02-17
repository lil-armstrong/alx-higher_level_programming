#!/usr/bin/python3

"""Define unittest for models.rectangle"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle_initialization(unittest.TestCase):
    """unittest suite for rectangle class"""

    def has_docs(self):
        """Everything is documented in models.rectangle"""
        self.assertTrue(len(Rectangle.__doc__) > 10)
