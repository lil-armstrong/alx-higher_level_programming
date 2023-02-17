#!/usr/bin/python3
"""Define unittest for models.base"""

import os
import unittest
from models.base import Base


class TestBase (unittest.TestCase):
    """Unittest for testing Base class"""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual()
