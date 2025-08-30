"""Tests for bootcamp."""
import unittest

import bootcamp


# Slicing:
#   [start:stop:step]
#   start
#   stop - stop BEFORE this, last one
#   step

class BootcampTestCase(unittest.TestCase):
    """Tests"""

    def testEvenOdd(self):
        a = [3, 4, 5, 6, 7]
        bootcamp.even_odd(a)
        self.assertListEqual([6, 4, 5, 7, 3], a)

        a = [3, 3, 3, 3, 3]
        bootcamp.even_odd(a)
        self.assertListEqual([3, 3, 3, 3, 3], a)

    def testBasics(self):
        a = [1, 6, 3, 4, 5, 2, 7]
        self.assertListEqual([3, 4], a[2:4])
        self.assertListEqual([3, 4, 5, 2, 7], a[2:])
        self.assertListEqual([1, 6, 3, 4], a[:4])
        self.assertListEqual([1, 6, 3, 4, 5, 2], a[:-1])
        self.assertListEqual([6, 4], a[1:5:2])
        self.assertListEqual([2, 4], a[5:1:-2])
        self.assertListEqual([7, 2, 5, 4, 3, 6, 1], a[::-1])

        # Also: b = a[:] # rotate

        # List comp.
        self.assertListEqual([0, 1, 4, 9, 16, 25], [a ** 2 for a in range(6)])
        self.assertListEqual([0, 4, 16],
                             [a ** 2 for a in range(6) if a % 2 == 0])

    def testShuffleInPlace(self):
        a = ['a', 'b', 'c', 'd']
        bootcamp.shuffle_in_place(a)
        print(a)

    def testShuffle(self):
        a = ['a', 'b', 'c', 'd']
        result = bootcamp.shuffle_sort(a)
        print(result)

    def testShuffleSort(self):
        a = [1, 2, 3, 4]
        p = [36, 3, 62, 19]
        self.assertEqual([2, 4, 1, 3], bootcamp.shuffle_sort_ex(a, p))

        # p has dups
        p = [36, 36, 62, 19]
        self.assertEqual([4, 1, 1, 3], bootcamp.shuffle_sort_ex(a, p))

    def testInitArray(self):
        n = 3
        w = [[0] * n for _ in range(n)]
        print(w)


if __name__ == '__main__':
    unittest.main()
