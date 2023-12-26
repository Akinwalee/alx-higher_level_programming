#!/usr/bin/python3
import unittest

"""Unittest for max_integer(list=[]) function"""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test cases
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([0, -1, -4, -99, -5]), 0)
        self.assertAlmostEqual(max_integer([9]), 9)
