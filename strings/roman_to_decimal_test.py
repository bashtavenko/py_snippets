"""Tests for roman to decimal."""
import unittest

import roman_to_decimal as m


class RomanTestCase(unittest.TestCase):
    def testConvert(self):
        self.assertEqual(99, m.roman_to_decimal('IC'))


if __name__ == '__main__':
    unittest.main()
