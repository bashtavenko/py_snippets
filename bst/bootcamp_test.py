"""Tests for BST basics.
      20
  10        30
8    12  25    40
"""

import unittest

import bootcamp as b


class BootcampTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = b.BSTNode(
            20,
            left=b.BSTNode(10, left=b.BSTNode(8), right=b.BSTNode(12)),
            right=b.BSTNode(30, left=b.BSTNode(25), right=b.BSTNode(40)),
        )

    def testGetMin(self):
        self.assertEqual(8, b.get_min(self.tree).data)
        self.assertEqual(8, b.get_min_iterative(self.tree).data)

    def testSearch(self):
        self.assertIsNotNone(b.search(self.tree, 10))
        self.assertIsNone(b.search(self.tree, 101))

    def testSearchIterative(self):
        self.assertIsNotNone(b.search_iterative(self.tree, 10))
        self.assertIsNone(b.search_iterative(self.tree, 101))

    def testIterativeInOrder(self):
        b.iterative_inorder(self.tree)

    def testSuccessor(self):
        b.find_successor(self.tree)


if __name__=="__main__":
    unittest.main()
