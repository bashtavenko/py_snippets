"""Tests for max sum."""

import unittest

import max_sum as m


class MaxSumTestCase(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(15, m.max_sum_o_square([3, 1, 5, 2, 9, 10, 4]))
        self.assertEqual(17, m.max_sum_o_square([1, 6, 0, 7, 0, 10, 0]))


if __name__=="__main__":
    unittest.main()
