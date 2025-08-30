"""Tests for merge two sorted."""

import unittest

import bootcamp as b
import is_bst as m


class IsBstTestCase(unittest.TestCase):

    def setUp(self):
        self.valid_tree = b.BSTNode(
            15,
            left=b.BSTNode(10, left=b.BSTNode(5), right=b.BSTNode(12)),
            right=b.BSTNode(25, left=b.BSTNode(20), right=b.BSTNode(30)),
        )

        self.invalid_tree = b.BSTNode(
            15,
            left=b.BSTNode(10, left=b.BSTNode(5), right=b.BSTNode(12)),
            right=b.BSTNode(25, left=b.BSTNode(13), right=b.BSTNode(30)),
        )

    def testIsBst(self):
        self.assertTrue(m.is_bst(self.valid_tree))
        self.assertFalse(m.is_bst(self.invalid_tree))

    def testIsBstBfs(self):
        self.assertTrue(m.is_bst_bfs(self.valid_tree))
        self.assertFalse(m.is_bst_bfs(self.invalid_tree))


if __name__=="__main__":
    unittest.main()
