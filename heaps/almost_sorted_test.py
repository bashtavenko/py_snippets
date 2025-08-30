"""Tests for almost sored."""
import unittest

import almost_sorted as m


class AlmostSortedTestCase(unittest.TestCase):
    def testSorted(self):
        result = m.sort_almost_sorted([3, -1, 2, 6, 4, 5, 8], 2)
        self.assertListEqual([-1, 2, 3, 4, 5, 6, 8], result)


if __name__ == '__main__':
    unittest.main()
