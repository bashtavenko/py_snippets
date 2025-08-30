import unittest
import digraph

class MyTestCase(unittest.TestCase):
    """https://algs4.cs.princeton.edu/lectures/44ShortestPaths-2x2.pdf"""
    def test_add(self):
        graph = digraph.Digraph()
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 7, 8)
        graph.add_edge(0, 4, 9)
        graph.add_edge(1, 7, 4)
        graph.add_edge(1, 3, 15)
        graph.add_edge(1, 2, 12)
        graph.add_edge(2, 3, 3)
        graph.add_edge(2, 6, 11)
        graph.add_edge(3, 6, 9)
        graph.add_edge(4, 7, 5)
        graph.add_edge(4, 5, 4)
        graph.add_edge(4, 6, 20)
        graph.add_edge(5, 2, 1)
        graph.add_edge(5, 6, 13)
        graph.add_edge(7, 2, 7)
        graph.add_edge(7, 5, 6)
        graph.add_vertex(6)

        graph.run_classic_dijkstra(0)
        expected_dist_to = {
            0: 0,
            1: 5,   # 0 -> 1
            2: 14,  # 0 -> 4 -> 5 -> 2
            3: 17,  # 2 -> 3
            4: 9.0, # 0 -> 4
            5: 13,  # 4 -> 5
            6: 25,  # 2 -> 6
            7: 8    # 0 -> 7
        }
        self.assertEqual(expected_dist_to, graph.dist_to)


if __name__ == '__main__':
    unittest.main()
