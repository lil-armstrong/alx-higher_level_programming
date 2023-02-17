#!/usr/bin/python3
"""Define unittest for models.base"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittest suite for Square class"""

    def has_docs(self):
        """Everything is documented in models.square"""
        self.assertTrue(len(Rectangle.__doc__) > 10)
