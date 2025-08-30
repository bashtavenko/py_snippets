# -*- coding: latin-1 -*-
"""Tests for Dijkstra calc."""
import unittest

import dijkstra_calc as m


class DijkstraTestCase(unittest.TestCase):
    def testDiskstra(self):
        self.assertEqual(101, m.evaluate("(1+((2+3)*(4*5)))"))


if __name__ == "__main__":
    unittest.main()
