"""Tests for strings bootcamp."""

import unittest

import bootcamp as m


class BootcampTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [1, 3, 6, 7, 9, 25]
        # self.function = m.binary_search_i
        self.function = m.binary_search_r

    def testBinarySearch(self):
        self.assertEqual(2, self.function(self.data, 4))
        self.assertEqual(6, self.function(self.data, 30))
        self.assertEqual(3, self.function(self.data, 7))
        self.assertEqual(5, self.function(self.data, 25))
        self.assertEqual(0, self.function(self.data, 1))


if __name__ == "__main__":
    unittest.main()
