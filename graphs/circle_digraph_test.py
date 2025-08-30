"""Tests for digraph cycles."""
import unittest
import collections

import circle_digraph as m
import bootcamp as b

class CircleTestCase(unittest.TestCase):
    def testDetect_NoCircle(self):
      graph = collections.defaultdict(set)

      graph[1].add(2)
      graph[2].add(4)
      graph[1].add(3)
      graph[3].add(4)

      # 4 is hit twice but that's ok because it's a cross edge
      self.assertFalse(m.detect_cycle(graph))

    def testDetect_Circle(self):
      graph = collections.defaultdict(set)

      graph[1].add(2)
      graph[2].add(3)
      graph[3].add(1)

      # 3 -> 1 is back edge
      self.assertTrue(m.detect_cycle(graph))

    def testDetectEx_NoCircle(self):
        graph = collections.defaultdict(set)

        one = b.GraphNode(1)
        two = b.GraphNode(2)
        three = b.GraphNode(3)
        four = b.GraphNode(4)

        graph[one].add(two)
        graph[two].add(four)
        graph[one].add(three)
        graph[three].add(four)

        # 4 is hit twice but that's ok because it's a cross edge
        self.assertFalse(m.detect_cycle_ex(graph))

    def testDetectEx_Circle(self):
        graph = collections.defaultdict(set)

        one = b.GraphNode(1)
        two = b.GraphNode(2)
        three = b.GraphNode(3)

        graph[one].add(two)
        graph[two].add(three)
        graph[three].add(one)

        # 4 is hit twice but that's ok because it's a cross edge
        self.assertFalse(m.detect_cycle_ex(graph))


if __name__ == '__main__':
    unittest.main()
