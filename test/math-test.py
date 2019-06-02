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
        self.assertEqual(Math.addition(3, 4), 8)
