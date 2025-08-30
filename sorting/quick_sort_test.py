"""Tests for Quick Sort."""
import unittest

import quick_sort as m

class QuickSortTestCase(unittest.TestCase):

    def testPartition(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        expected = [2, 1, 3, 4, 7, 5, 6, 8]
        i = m.partition(a, 0, len(a) - 1)
        self.assertEqual(3, i)
        self.assertListEqual(expected, a)

    def testSort(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        m.quick_sort(a, 0, len(a) - 1)
        self.assertListEqual(expected, a)

    def testRandomizedSort(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        m.randomized_quick_sort(a, 0, len(a) - 1)
        self.assertListEqual(expected, a)

    def testSelect(self):
        a = [3, 2, 1, 5, 4]
        self.assertEqual(2, m.select(a, 2))
        self.assertEqual(1, m.select(a, 1))
        self.assertEqual(3, m.select(a, 3))
        self.assertEqual(4, m.select(a, 4))
        self.assertEqual(5, m.select(a, 5))


if __name__ == '__main__':
    unittest.main()
