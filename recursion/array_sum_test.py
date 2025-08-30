import unittest

import array_sum as m


class SumTestCase(unittest.TestCase):

  def setUp(self):
    self.data = [1,[11,42,[8, 1], 4, [22,21]]]

  def testCalcSum(self):
    self.assertEqual(110, m.calc_sum(self.data))

  def testCalcSumRecursive(self):
    self.assertEqual(6, m.cal_sum_recursive([1, 2, 0, 3]))
    self.assertEqual(14, m.cal_sum_recursive([1, 2, [1, 2], 3, [5]]))
    self.assertEqual(110, m.cal_sum_recursive(self.data))

  def testCalcSumRecursive(self):
    self.assertEqual(6, m.cal_sum_recursive_basic([1, 2, 0, 3]))

if __name__ == '__main__':
  unittest.main()
