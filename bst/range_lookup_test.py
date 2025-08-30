"""Tests for range lookup."""
import unittest

import range_lookup as m

class RangeLookupTestCase(unittest.TestCase):

  def setUp(self):
    self.tree = m.BSTNode(
        50,
        left=m.BSTNode(20, right=m.BSTNode(21, left=m.BSTNode(12))),
        right=m.BSTNode(75, right=m.BSTNode(80), left=m.BSTNode(65)))

  def testRangeLookup(self):
    result = m.range_lookup (self.tree, 15, 30)
    self.assertListEqual([20, 21], result)

if __name__ == '__main__':
  unittest.main()
