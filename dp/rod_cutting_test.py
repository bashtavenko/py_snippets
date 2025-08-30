import unittest

import rod_cutting as m


class RodCuttingTestCase(unittest.TestCase):

    def testRodCutting(self):
      self.assertEqual(10, m.cut_rod(4))

    def testRodCuttingMemoization(self):
        self.assertEqual(10, m.cut_rod_memoized(4))
        self.assertEqual(18, m.cut_rod_memoized(7))

    def testRodCuttingBottomUp(self):
        self.assertEqual(10, m.cut_rod_bottom_up(4))

    def testRodCuttingBottomUpPath(self):
        result = m.cut_rod_bottom_up_path(4)
        self.assertEqual(10, result.Revenue)
        self.assertListEqual([2, 2], result.Path)

        result = m.cut_rod_bottom_up_path(10)
        self.assertEqual(30, result.Revenue)
        self.assertListEqual([10], result.Path)

        result = m.cut_rod_bottom_up_path(7)
        self.assertEqual(18, result.Revenue)
        self.assertListEqual([1, 6], result.Path)


if __name__ == '__main__':
    unittest.main()
