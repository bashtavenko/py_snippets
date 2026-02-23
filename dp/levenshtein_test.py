"""Levenshtein test."""

import unittest
import dp.levenshtein as levenshtein


class MyTestCase(unittest.TestCase):

    def test_basic_1(self):
        self.assertEqual(8, levenshtein.levenshtein_distance('carthorse', 'orchestra'))

    def test_basic_2(self):
        self.assertEqual(3, levenshtein.levenshtein_distance('saturday', 'sunday'))

    def test_same(self):
        self.assertEqual(0, levenshtein.levenshtein_distance('saturday', 'saturday'))

if __name__ == '__main__':
    unittest.main()

