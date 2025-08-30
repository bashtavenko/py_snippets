"""Tests for height balanced."""

import unittest

import bootcamp as b
import height_balanced as m


class HeightBalancedTestCase(unittest.TestCase):

    def testIsBalanced_Balanced(self):
        root = b.BinaryTreeNode(
            data="a",
            left=b.BinaryTreeNode(
                data="b",
                left=b.BinaryTreeNode(data="c"),
                right=b.BinaryTreeNode(data="d"),
            ),
            right=b.BinaryTreeNode(data="e"),
        )

        result = m.is_balanced(root)
        self.assertTrue(result)

    def testIsBalanced_NotBalanced(self):
        root = b.BinaryTreeNode(
            data="a",
            left=b.BinaryTreeNode(
                data="b",
                left=b.BinaryTreeNode(data="c", left=b.BinaryTreeNode(data="d")),
                right=b.BinaryTreeNode(data="e"),
            ),
        )

        result = m.is_balanced(root)
        self.assertFalse(result)


if __name__=="__main__":
    unittest.main()
