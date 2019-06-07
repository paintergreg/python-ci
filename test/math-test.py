#! /usr/bin/env python3
#
################
#
# test/math-test.py
#
################
#

"""
docstring goes here.  be sure to write a good one ;)
"""

import unittest
from src.math import Math


class MathTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Math.addition(3, 4), 7)

    def test_invalid_add_value1(self):
        self.assertEqual(Math.addition("A", 3), "value1 Invalid Input")

    def test_invalid_add_value2(self):
        self.assertEqual(Math.addition(2, "A"), "value2 Invalid Input")

    def test_subtraction(self):
        self.assertEqual(Math.subtraction(12, 4), 8)

    def test_invalid_sub_value1(self):
        self.assertEqual(Math.subtraction("A", "A"), "Invalid Input")

    def test_invalid_sub_value2(self):
        self.assertEqual(Math.subtraction("A", "A"), "Invalid Input")
