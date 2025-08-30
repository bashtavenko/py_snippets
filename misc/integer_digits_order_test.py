"""Tests for histogram bootcamp."""

import unittest

import integer_digits_order as m


class DigitsTestCase(unittest.TestCase):

    def testDigits(self):
        self.assertTrue(m.is_sorted(123456))
        self.assertTrue(m.is_sorted(654321))
        self.assertFalse(m.is_sorted(126543))
        self.assertTrue(m.is_sorted(12))


if __name__=="__main__":
    unittest.main()
