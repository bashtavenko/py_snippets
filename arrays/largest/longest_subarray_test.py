"""Tests for longest consecutive subarray."""

import unittest

import longest_subarray as m


class LongestSubarrayTestCase(unittest.TestCase):

    def testGetSubarray(self):
        self.assertEqual([1, 2, 4], m.get_longest_subarray([1, 2, 1, 2, 4, 1]))
        self.assertEqual([2, 3], m.get_longest_subarray([2, 3, 1, 5, 0, 7, 2, 8]))
        self.assertEqual([1, 4, 6], m.get_longest_subarray([9, 0, 2, 1, 4, 6, 5, 3]))


if __name__ == "__main__":
    unittest.main()
