"""Tests for strings bootcamp."""

import unittest

import bootcamp as m


class BootcampTestCase(unittest.TestCase):
    def setUp(self):
        c = m.BinaryTreeNode(
            data=271, left=m.BinaryTreeNode(data=28), right=m.BinaryTreeNode(data=0)
        )
        b = m.BinaryTreeNode(
            data=6,
            left=c,
            right=m.BinaryTreeNode(
                data=561, right=m.BinaryTreeNode(data=3, left=m.BinaryTreeNode(data=17))
            ),
        )

        k = m.BinaryTreeNode(
            data=1, left=m.BinaryTreeNode(data=401, right=m.BinaryTreeNode(data=641))
        )

        i = m.BinaryTreeNode(
            data=6,
            left=m.BinaryTreeNode(data=2, right=k),
            right=m.BinaryTreeNode(data=271, right=m.BinaryTreeNode(28)),
        )

        self.root = m.BinaryTreeNode(data=314, left=b, right=i)

    def testTraversal(self):
        m.traverse_preorder(self.root)
        m.traverse_inorder(self.root)
        m.traverse_postorder(self.root)


if __name__ == "__main__":
    unittest.main()
