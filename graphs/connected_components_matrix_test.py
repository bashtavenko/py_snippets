"""Tests for connected components in matrix."""
import unittest

import connected_components_matrix as m


class ConnectedComponentMatrixTestCase(unittest.TestCase):
  def setUp(self):
      self.matrix = [[1, 1, 1, 1, 1],
                     [1, 0, 1, 1, 1],
                     [0, 0, 1, 1, 1],
                     [1, 1, 0, 1, 1],
                     [1, 1, 0, 0, 1],
                     [1, 1, 0, 0, 1],
                     [0, 0, 1, 1, 1]]

  def testGetComponents(self):
      result = m.get_components(self.matrix)
      self.assertEqual(3, len(result))
      self.assertListEqual([(2 , 0), (1, 1), (2, 1)], list(result[0]))


if __name__ == '__main__':
  unittest.main()
