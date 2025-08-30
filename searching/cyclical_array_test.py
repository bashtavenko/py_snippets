"""Tests for cyclical array."""

import unittest

import cyclical_array as m


class CyclicalTestCase(unittest.TestCase):

    def testCyclical(self):
        a = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
        self.assertEqual(4, m.search_smallest(a))

        self.assertEqual(1, m.search_smallest([6, 1, 2, 3, 4, 5]))

        self.assertEqual(3, m.search_smallest([6, 5, 4, 3, 2, 1, 7]))


if __name__=="__main__":
    unittest.main()
