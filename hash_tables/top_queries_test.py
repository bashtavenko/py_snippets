"""Tests for top queries."""
import unittest

import top_queries as m

class TopQueriesTestCase(unittest.TestCase):
    def setUp(self):
        self.strings = ['python', 'javascript', 'python',
            'javascript', 'python objects', 'javascript']
        self.expected = ['javascript (3)', 'python (2)',
                'python objects (1)']

    def testQueries_1(self):
        result = m.compute_very_crude(self.strings, 3)
        self.assertEqual(self.expected, result)

    def testQueries_2(self):
        result = m.compute_default_dict(self.strings, 3)
        self.assertEqual(self.expected, result)

    def testQueries_3(self):
        result = m.compute_counter(self.strings, 3)
        self.assertEqual(self.expected, result)

    def testQueries_4(self):
        result = m.compute_min_heap(iter(self.strings), 3)
        #self.assertEqual(['javascript (3)', 'python (2)'],
        #        result)

if __name__ == '__main__':
    unittest.main()
