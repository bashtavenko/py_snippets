"""Tests for first greater."""

import unittest

import bootcamp as b
import first_greater as m


class FirstGreaterTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = b.BSTNode(
            43,
            left=b.BSTNode(29, right=b.BSTNode(37, left=b.BSTNode(23))),
            right=b.BSTNode(47, right=b.BSTNode(53)),
        )

    def testFind(self):
        self.assertEqual(29, m.find(self.tree, 23).data)
        self.assertEqual(37, m.find(self.tree, 29).data)
        self.assertIsNone(m.find(self.tree, 53))
        self.assertEqual(43, m.find(self.tree, 37).data)

    def testFind_case1(self):
        tree = b.BSTNode(
            9, right=b.BSTNode(50, left=b.BSTNode(10), right=b.BSTNode(50))
        )
        self.assertEqual(10, m.find(tree, 9).data)

    def testFind_case2(self):
        tree = b.BSTNode(15, left=b.BSTNode(6), right=b.BSTNode(7, right=b.BSTNode(13)))
        self.assertEqual(15, m.find(tree, 13).data)

    def testFindBF(self):
        self.assertEqual(29, m.find_bf(self.tree, 23).data)
        self.assertEqual(37, m.find_bf(self.tree, 29).data)
        self.assertIsNone(m.find_bf(self.tree, 53))


if __name__=="__main__":
    unittest.main()
