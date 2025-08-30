"""Tests for flip color."""
import unittest

import flip_color as m


class FlipColorTestCase(unittest.TestCase):

  def setUp(self):
    self.matrix = [[1, 0, 1],
                   [1, 0, 1],
                   [0, 0, 1]]

  def testFlipBfs(self):
     m.flip_color_bfs(0, 1, self.matrix)
     self.assertListEqual(
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]], self.matrix)

  def testFlipBfs_2(self):
     m.flip_color_bfs(0, 0, self.matrix)
     self.assertListEqual(
         [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]], self.matrix)

  def testFlipDfs(self):
     m.flip_color_dfs(0, 1, self.matrix)
     self.assertListEqual(
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]], self.matrix)

  def testFlipDfs_2(self):
     m.flip_color_dfs(0, 0, self.matrix)
     self.assertListEqual(
         [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]], self.matrix)


if __name__ == '__main__':
  unittest.main()
