"""Tests for RPN calculator."""

import unittest

import reverse_polish as m


class ReversePolishTestCase(unittest.TestCase):

    def testReversePolish(self):
        self.assertEqual(7, m.evaluate("3 4 +"))
        self.assertEqual(15, m.evaluate("3 4 + 2 * 1 +"))


if __name__ == "__main__":
    unittest.main()
