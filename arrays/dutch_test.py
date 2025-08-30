import unittest

import dutch as m

class DutchTestCase(unittest.TestCase):
    long_message = True

    def testDutch_Classic(self):
        a = [3, 0, 1, 2, 3, 4, 1, 5]
        result = m.dutch(a)
        self.assertEquals((4, 5, 6), result)
        pivot = a[result[2] - 1]
        self.assertEquals(pivot, 3)
        # V = 3
        # < V, =V, > V
        # But elements to the left or right NOT SORTED
        self.assertListEqual([0, 1, 2, 1, 3, 3, 5, 4], a)

    def testDutch_NoLess(self):
        a = [0, 1, 2, 0, 2, 1, 1]
        m.dutch(a)
        # There are no less than 0
        # =V, > V
        self.assertListEqual([0, 0, 2, 2, 1, 1, 1], a)

    def testDutch_Classic_NoGreater(self):
        a = [2, 0, 0, 1, 2, 1]
        m.dutch(a)
        # V = 2
        # < V, =V
        self.assertListEqual([0, 0, 1, 1, 2, 2], a)

    def testDutch_Mixed(self):
        a = [2, 3, 1, 5, 7, 4, 9, 2]
        m.dutch(a)
        # V = 2
        # < V, =V
        self.assertListEqual([1, 2, 2, 7, 4, 9, 5, 3], a)

if __name__ == '__main__':
    unittest.main()
