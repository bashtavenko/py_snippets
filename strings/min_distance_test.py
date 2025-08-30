"""Tests for strings bootcamp."""

import unittest

import min_distance


class DistanceTestCase(unittest.TestCase):

    def testFind(self):
        result = min_distance.find("abxcdeymx", "x", "y")
        self.assertEqual(2, result)

    def testFind_2(self):
        result = min_distance.find("tbycdx", "x", "y")
        self.assertEqual(3, result)

    def testFind_3(self):
        result = min_distance.find("tbycdq", "x", "y")
        self.assertEqual(-1, result)

    def test_binary_search(self):
        a = [1, 3, 7, 9, 11, 17, 19, 21, 30]
        result = min_distance.find_first_greater_index(a, 9)
        self.assertEqual(4, result)

        result = min_distance.find_first_greater_index(a, 8)
        self.assertEqual(3, result)

        result = min_distance.find_first_greater_index(a, 22)
        self.assertEqual(8, result)

    def test_find_list(self):
        x_list = [1, 3, 7]
        y_list = [4, 8, 11]
        result = min_distance.find_with_list(x_list, y_list)
        self.assertEqual(1, result)

        x_list = [1, 3]
        y_list = [4, 9, 12]
        result = min_distance.find_with_list(x_list, y_list)
        self.assertEqual(1, result)

        x_list = [1, 3, 7]
        y_list = [4, 9, 12, 27]
        result = min_distance.find_with_list(x_list, y_list)
        self.assertEqual(1, result)

    def test_find_2d(self):
        data = ["xobcu", "zoyam", "tpxij"]


if __name__=="__main__":
    unittest.main()
