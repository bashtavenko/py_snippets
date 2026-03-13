import unittest

from misc.ica import queries


class QueriesTests(unittest.TestCase):
    failureException = Exception

    def setUp(self):
        self.container = queries

    def test_queries_all(self):
        queries = [["ADD", "0"],
                   ["ADD", "1"],
                   ["ADD", "1"],
                   ["ADD", "11"],
                   ["ADD", "22"],
                   ["ADD", "3"],
                   ["ADD", "5"],
                   ["GET_NEXT", "0"],
                   ["GET_NEXT", "1"],
                   ["REMOVE", "1"],
                   ["GET_NEXT", "1"],
                   ["ADD", "0"],
                   ["ADD", "1"],
                   ["ADD", "2"],
                   ["ADD", "1"],
                   ["GET_NEXT", "1"],
                   ["GET_NEXT", "2"],
                   ["GET_NEXT", "3"],
                   ["GET_NEXT", "5"]]

        self.assertEqual(self.container.solution(queries),["", "", "", "", "", "", "", "1", "3", "true", "3", "", "", "", "", "2", "3", "5", "11"])


if __name__ == '__main__':
    unittest.main()
