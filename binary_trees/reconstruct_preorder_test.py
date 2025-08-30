"""Tests for reconstruct."""

import unittest

import reconstruct_preorder as m


class ReconstructTestCase(unittest.TestCase):
    def testConstructSimple(self):
        preorder = [1, 2, None, None, 3, None, None]
        result = m.reconstruct(preorder)
        self.assertEqual(1, result.data)
        self.assertEqual(2, result.left.data)
        self.assertEqual(3, result.right.data)


if __name__=="__main__":
    unittest.main()
