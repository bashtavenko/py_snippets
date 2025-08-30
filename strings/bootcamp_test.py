"""Tests for strings bootcamp."""

import unittest

import bootcamp


class StringsBootcampTestCase(unittest.TestCase):
    def testIsPalindrome(self):
        self.assertTrue(bootcamp.is_palindromic([1, 2, 3, 4, 3, 2, 1]))


if __name__=="__main__":
    unittest.main()
