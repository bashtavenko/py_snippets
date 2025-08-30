import unittest

import maze as m


class MyTestCase(unittest.TestCase):

    def test_search_maze(self):
        maze = [[1, 0, 0], [0, 0, 1], [1, 0, 1]]
        path = m.search_maze(maze, m.Coordinate(2, 1), m.Coordinate(0, 2))
        print(path)


if __name__=="__main__":
    unittest.main()
