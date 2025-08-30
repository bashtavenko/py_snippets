"""Tests for max subarray."""
import unittest

import max_subarray as m


class MaxSubarrayTestCase(unittest.TestCase):

  def testThree_3(self):
    a = [4, -1, 2]
    result = m.max_subarray(a)
    self.assertEqual((0, 2, 5), result)

  def testBasic(self):
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    result = m.max_subarray(a)
    self.assertEqual((7, 10, 43), result)

  def testOne(self):
    a = [3, -2]
    result = m.max_subarray(a)
    self.assertEqual((0, 0, 3), result)

  def testOne_2(self):
    a = [2, 3]
    result = m.max_subarray(a)
    self.assertEqual((0, 1, 5), result)

  def testThree(self):
    a = [2, -1, 7]
    result = m.max_subarray(a)
    self.assertEqual((0, 2, 8), result)

  def testThree_2(self):
    a = [7, -1, 2]
    result = m.max_subarray(a)
    self.assertEqual((0, 2, 8), result)

  def testTwo(self):
    a = [1, 2, -1, 2]
    result = m.max_subarray(a)
    self.assertEqual((0, 3, 4), result)

  def testFour_right(self):
    a = [1, -4, 3, -4]
    result = m.max_subarray(a)
    self.assertEqual((2, 2, 3), result)

  def testFour_crossing(self):
    a = [2, 3, 7, -1]
    result = m.max_subarray(a)
    self.assertEqual((0, 2, 12), result)

  def testFour_crossing_2(self):
    a = [3, 7, 2, -1]
    result = m.max_subarray(a)
    self.assertEqual((0, 2, 12), result)

  def testFour_left(self):
    a = [4, 1, 2, -1]
    result = m.max_subarray(a)
    self.assertEqual((0, 2, 7), result)

  def testNine(self):
      a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
      result = m.max_subarray(a)
      self.assertEqual((3, 6, 6), result)

if __name__ == '__main__':
  unittest.main()
