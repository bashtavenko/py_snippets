"""Tests for strings bootcamp."""

import unittest

import merge_sorted_arrays as m


class MergeArraysTestCase(unittest.TestCase):

    def testMerge(self):
        result = m.merge_sorted_arrays(([3, 5, 7], [0, 6], [0, 6, 28]))
        self.assertListEqual([0, 0, 3, 5, 6, 6, 7, 28], result)


if __name__ == "__main__":
    unittest.main()
