import unittest

import largest_pair as m


class MaxSumTestCase(unittest.TestCase):
    def testGetLargestPair(self):
        a = [2, 3, 10, 6, 4, 8, 1]
        self.assertTupleEqual((10, 8), m.get_largest_pair(a))

        a = [8, 6, 4, 3, 2, 1]
        self.assertTupleEqual((8, 6), m.get_largest_pair(a))

        a = [2, 2, 2, 2, 2, 2]
        self.assertTupleEqual((), m.get_largest_pair(a))

        a = [2, 3]
        self.assertTupleEqual((3, 2), m.get_largest_pair(a))

        a = [2]
        self.assertTupleEqual((), m.get_largest_pair(a))

        self.assertTupleEqual((), m.get_largest_pair([]))


if __name__ == "__main__":
    unittest.main()
