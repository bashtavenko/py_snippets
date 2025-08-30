# -*- coding: latin-1 -*-
"""Tests for PN calculator."""
import unittest

import polish as m


class PolishTestCase(unittest.TestCase):
    def setUp(self):
        self.f = [m.calculate, m.calculate_lor]

    def testPolish(self):
        for func in self.f:
            self.assertEqual(7, func("+ 3 4"))
            # Not sure if this even a valid test case in Polish notation
            # self.assertEquals(8, func('+ 1 3 4'))
            self.assertEqual(-7, func("* - 5 6 7"), func)
            self.assertEqual(-37, func("- 5 * 6 7"))
            self.assertEqual(5, func("- * / 15 - 7 + 1 1 3 + 2 + 1 1"))


if __name__ == "__main__":
    unittest.main()
