import unittest

import sequence_2d_array as m


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.grid = [[1, 2, 3],
                     [3, 4, 5],
                     [5, 6, 7]]

    def testRun(self):
        self.assertTrue(m.is_pattern_found(self.grid, [1, 3, 4, 6]))
        self.assertFalse(m.is_pattern_found(self.grid, [1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()
