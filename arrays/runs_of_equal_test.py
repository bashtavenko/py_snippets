import unittest
import runs_of_equal as m


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(3, m.count_consecutive([3, 3, 3, 4, 2, 2, 4, 4]))
        self.assertEqual(2, m.count_consecutive([3, 3, 3, 4, 2, 2, 7, 8]))
        self.assertEqual(0, m.count_consecutive([1, 3, 1, 4, 2, 9, 7, 8]))

    def test_part_one_2(self):
        self.assertEqual(3, m.count_consecutive_2([3, 3, 3, 4, 2, 2, 4, 4]))
        self.assertEqual(2, m.count_consecutive_2([3, 3, 3, 4, 2, 2, 7, 8]))
        self.assertEqual(0, m.count_consecutive_2([1, 3, 1, 4, 2, 9, 7, 8]))

    def test_edge_cases(self):
        self.assertEqual(0, m.count_consecutive([1, 2, 3]))
        self.assertEqual(0, m.count_consecutive([]))

    def test_part_two(self):
        self.assertEqual(2, m.count_consecutive_part2([3, 3, 4, 4, 3, 3]))


if __name__ == '__main__':
    unittest.main()
