"""Tests for number_twice_once."""
import unittest

import number_twice_once as m


class NumberTwiceTestCase(unittest.TestCase):
    def setUp(self):
        self.funcs = [m.find, m.find_2, m.find_xor, m.find_binary_search]

    def testNumber(self):
        for f in self.funcs:
            self.assertEqual(5, f([1, 1, 3, 3, 5, 6, 6]))
            self.assertEqual(5, f([1, 1, 3, 3, 5]))
            self.assertEqual(3, f([1, 1, 3, 5, 5, 6, 6]))
            self.assertEqual(1, f([1, 4, 4, 5, 5, 6, 6]))
            self.assertEqual(2, f([2, 4, 4]))


if __name__ == '__main__':
    unittest.main()
