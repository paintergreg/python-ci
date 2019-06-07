#! /usr/bin/env python3
#
################
#
# src/math.python
#
################
#

"""
docstring goes here.  be sure to write a good one ;)
"""


class Math:
    def addition(value1: int, value2: int) -> int:
        if not isinstance(value1, int) or not isinstance(value2, int):
            return "Invalid Input"
        else:
            return value1 + value2

    def subtraction(value1: int, value2: int) -> int:
        if not isinstance(value1, int) or not isinstance(value2, int):
            return "Invalid Input"
        else:
            return value1 - value2
