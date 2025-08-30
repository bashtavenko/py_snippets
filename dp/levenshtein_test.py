"""Levenshtein test."""

import unittest
import levenshtein


class MyTestCase(unittest.TestCase):

    def test_basic_1(self):
        self.assertEquals(8, levenshtein.levenshtein_distance('carthorse', 'orchestra'))

    def test_basic_2(self):
        self.assertEquals(3, levenshtein.levenshtein_distance('saturday', 'sunday'))

    def test_same(self):
        self.assertEquals(0, levenshtein.levenshtein_distance('saturday', 'saturday'))

if __name__ == '__main__':
    unittest.main()

