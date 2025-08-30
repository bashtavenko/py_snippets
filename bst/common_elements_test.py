"""Tests for common elements in BST.

       20
  10        30
8    12  25    40

        22
    11         30
 8     13  27     40

Should result in: [8, 30, 40]
"""
import unittest

import common_elements as m
import bootcamp as b


class CommonElementsTestCase(unittest.TestCase):

  def testFindCommon(self):
      tree1 = b.BSTNode(
          20,
          left=b.BSTNode(10, left=b.BSTNode(8), right=b.BSTNode(12)),
          right=b.BSTNode(30, left=b.BSTNode(25), right=b.BSTNode(40))
      )

      tree2 = b.BSTNode(
          22,
          left=b.BSTNode(11, left=b.BSTNode(8), right=b.BSTNode(13)),
          right=b.BSTNode(30, left=b.BSTNode(30), right=b.BSTNode(40))
      )
      self.assertListEqual(m.find_common(tree1, tree2), [8, 30, 40])

  def testFindCommonDifferentHeight(self):
      tree1 = b.BSTNode(
          20,
          left=b.BSTNode(10, left=b.BSTNode(8), right=b.BSTNode(12)),
          right=b.BSTNode(30, left=b.BSTNode(25), right=b.BSTNode(40))
      )

      tree2 = b.BSTNode(11, left=b.BSTNode(8), right=b.BSTNode(13))
      self.assertListEqual(m.find_common(tree1, tree2), [8])


  def testIterator(self):
      tree = b.BSTNode(11, left=b.BSTNode(8), right=b.BSTNode(13))
      tree_iter = m.BstIterator(tree)
      self.assertEqual([8, 11, 13], list(tree_iter));


if __name__ == '__main__':
  unittest.main()
