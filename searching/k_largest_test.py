"""Tests for strings bootcamp."""

import unittest

import k_largest as m


class KlargestTestCase(unittest.TestCase):

    def testfind(self):
        a = [3, 2, 1, 5, 4]
        self.assertEqual(4, m.find_kth_largest(2, a))
        self.assertEqual(3, m.find_kth_largest(3, a))
        self.assertEqual(4, m.find_kth_largest(2, a))

    def testFindHeap(self):
        a = [3, 2, 1, 5, 4]
        self.assertEqual(4, m.find_kth_heap(2, a))
        self.assertEqual(3, m.find_kth_heap(3, a))
        self.assertEqual(4, m.find_kth_heap(2, a))


if __name__=="__main__":
    unittest.main()
