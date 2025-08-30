import unittest

import max_gold as m


class MaxGoldTestCase(unittest.TestCase):
    long_message = True

    def testGetMax(self):
        self.assertEqual(17, m.get_max([10, 8, 7, 1, 8]))
        self.assertEqual(32, m.get_max([8, 0, 8, 0, 0, 8, 0, 8, 1]))
        self.assertEqual(22, m.get_max([1, 7, 2, 7, 3, 8]))
        self.assertEqual(17, m.get_max([7, 6, 0, 6, 0, 5]))

    def testGetMax2(self):
        self.assertEqual(17, m.get_max2([10, 8, 7, 1, 8]))
        self.assertEqual(32, m.get_max2([8, 0, 8, 0, 0, 8, 0, 8, 1]))
        self.assertEqual(22, m.get_max2([1, 7, 2, 7, 3, 8]))
        self.assertEqual(17, m.get_max2([7, 6, 0, 6, 0, 5]))

    def testGetMaxDemo(self):
        self.assertEqual(25, m.get_max_recursive_demo([10, 8, 7, 1, 8]))

    def testGetMaxCached(self):
        self.assertEqual(25, m.get_max_cached([10, 8, 7, 1, 8]))

if __name__ == '__main__':
    unittest.main()
