"""Tests for online median."""
import unittest

import online_median as m


class OnlineMedianTestCase(unittest.TestCase):
    def testOnlineMedian(self):
        stream = [1, 0, 3, 5, 2, 0, 1]
        self.assertListEqual([1, 0.5, 1, 2, 2, 1.5, 1],
                             m.online_median(iter(stream)))


if __name__ == '__main__':
    unittest.main()
