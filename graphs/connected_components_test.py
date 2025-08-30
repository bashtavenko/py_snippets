"""Tests for strings bootcamp."""
import unittest

import connected_components as m


class ConnectedComponentTestCase(unittest.TestCase):
  def setUp(self):
      input_edges = [
              m.InputEdge(0, 6),
              m.InputEdge(0, 2),
              m.InputEdge(0, 1),
              m.InputEdge(0, 5),
              m.InputEdge(5, 3),
              m.InputEdge(5, 4),
              m.InputEdge(3, 4),
              m.InputEdge(4, 6),
              m.InputEdge(7, 8),
              m.InputEdge(9, 10),
              m.InputEdge(9, 11),
              m.InputEdge(9, 12),
              m.InputEdge(11, 12)]
      self.graph = m.build_graph(input_edges)
      self.vertices = range(13)

  def testGetComponents(self):
      result = m.get_components(self.graph)
      self.assertEqual(3, len(result))
      self.assertListEqual([0, 1, 2, 3, 4, 5, 6], list(result[0]))


if __name__ == '__main__':
  unittest.main()
