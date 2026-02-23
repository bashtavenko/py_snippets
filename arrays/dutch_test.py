import unittest

import arrays.dutch as m


class DutchTestCase(unittest.TestCase):
    long_message = True

    def testDutch_Classic(self):
        a = [3, 0, 1, 2, 3, 4, 1, 5]
        result = m.dutch(a)
        self.assertEqual((0, 1, 2), result)
        pivot = a[result[2] - 1]
        self.assertEqual(pivot, 0)
        # V = 3
        # < V, =V, > V
        # But elements to the left or right NOT SORTED
        self.assertListEqual([3, 0, 2, 3, 4, 1, 5, 1], a)

    def testDutch_NoLess(self):
        a = [0, 1, 2, 0, 2, 1, 1]
        m.dutch(a)
        # There is no less than 0
        # =V, > V
        self.assertListEqual([0, 1, 1, 0, 1, 2, 2], a)

    def testDutch_Classic_NoGreater(self):
        a = [2, 0, 0, 1, 2, 1]
        m.dutch(a)
        # V = 2
        # < V, =V
        self.assertListEqual([2, 0, 0, 2, 1, 1], a)

    def testDutch_Mixed(self):
        a = [2, 3, 1, 5, 7, 4, 9, 2]
        m.dutch(a)
        # V = 2
        # < V, =V
        self.assertListEqual([1, 2, 2, 3, 4, 9, 7, 5], a)


if __name__ == '__main__':
    unittest.main()
