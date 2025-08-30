"""Tests for Insertion sort."""
import unittest

import insertion_sort as m

class InsertionSortTestCase(unittest.TestCase):

    def testSort(self):
        a = [5, 2, 4, 6, 1, 3]
        expected = [1, 2, 3, 4, 5, 6]
        m.insertion_sort(a)
        self.assertListEqual(expected, a)

if __name__ == '__main__':
    unittest.main()
