"""Tests for merge two sorted."""

import unittest

import merge_two_sorted as m


class MergeTwoSortedTestCase(unittest.TestCase):

    def testMerge(self):
        result = m.merge_arrays_ugly([3, 5, 7], [0, 6])
        self.assertListEqual([0, 3, 5, 6, 7], result)

    def testMerge_equal(self):
        result = m.merge_arrays_ugly([3, 5, 7, 9], [0, 5, 7, 11])
        self.assertListEqual([0, 3, 5, 7, 9, 11], result)

    def testMerge_2(self):
        result = m.merge_arrays([3, 5, 7], [1, 6])
        self.assertListEqual([1, 3, 5, 6, 7], result)

    def testMerge_21(self):
        a = [3, 5, 7]
        b = [1, 6]
        result = m.merge_arrays(a, b)
        self.assertListEqual([1, 3, 5, 6, 7], result)
        # It destructs the list
        self.assertEqual(1, len(a))
        self.assertEqual(0, len(b))

    def testMerge_22(self):
        result = m.merge_arrays([3, 5, 7], [0, 6])
        self.assertListEqual([0, 3, 5, 6, 7], result)


if __name__=="__main__":
    unittest.main()
