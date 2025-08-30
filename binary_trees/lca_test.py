"""Tests for LCA."""

import unittest

import bootcamp as b
import lca as m


class LcaTestCase(unittest.TestCase):

    def testBasic(self):
        c_node = b.BinaryTreeNode(data="c")
        d_node = b.BinaryTreeNode(data="d")
        b_node = b.BinaryTreeNode(data="b", left=c_node, right=d_node)
        e_node = b.BinaryTreeNode(data="e")
        a_node = b.BinaryTreeNode(data="a", left=b_node, right=e_node)

        c_node.parent = b_node
        d_node.parent = b_node
        b_node.parent = a_node
        e_node.parent = a_node

        result = m.find_lca(a_node, c_node, e_node)
        self.assertEqual("a", result.data)


if __name__=="__main__":
    unittest.main()
