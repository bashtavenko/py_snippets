"""Tests for reconstruct."""

import unittest

import reconstruct as m


class ReconstructTestCase(unittest.TestCase):
    def testConstruct(self):
        in_order = [4, 8, 2, 5, 1, 6, 3, 7]
        post_order = [8, 4, 5, 2, 6, 7, 3, 1]
        result = m.construct_tree(in_order, post_order)
        self.assertEqual(1, result.data)
        self.assertEqual(2, result.left.data)
        self.assertEqual(3, result.right.data)
        self.assertEqual(4, result.left.left.data)
        self.assertEqual(5, result.left.right.data)

    def testConstructSimple(self):
        in_order = [2, 1, 3]
        post_order = [2, 3, 1]
        result = m.construct_tree(in_order, post_order)
        self.assertEqual(1, result.data)
        self.assertEqual(2, result.left.data)
        self.assertEqual(3, result.right.data)


if __name__=="__main__":
    unittest.main()
