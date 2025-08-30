"""Tests for get_nth."""
import unittest

import get_nth as m


class SelectTestCase(unittest.TestCase):
    def setUp(self):
      self.tree = m.Node('a',
                        left=m.Node('b',
                                    left=m.Node('c', size=1),
                                    right=m.Node('d', right=m.Node('e', size=1),
                                                 size=2),
                                    size=4),
                        right=m.Node('f', size=1),
                        size=6)

    def testSelect(self):
      self.assertEqual('b', m.select(self.tree, 1).data)
      self.assertEqual('d', m.select(self.tree, 2).data)
      self.assertEqual('e', m.select(self.tree, 3).data)
      self.assertEqual('a', m.select(self.tree, 4).data)
      self.assertEqual('f', m.select(self.tree, 5).data)

    def testSelectIterative(self):
      self.assertEqual('b', m.select_iterative(self.tree, 1).data)
      self.assertEqual('d', m.select_iterative(self.tree, 2).data)
      self.assertEqual('e', m.select_iterative(self.tree, 3).data)
      self.assertEqual('a', m.select_iterative(self.tree, 4).data)
      self.assertEqual('f', m.select_iterative(self.tree, 5).data)


if __name__ == '__main__':
    unittest.main()
