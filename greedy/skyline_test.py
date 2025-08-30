import unittest

import skyline as m


class SkylineTestCase(unittest.TestCase):
    long_message = True

    def testCalc(self):
        heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
        self.assertEqual(20, m.calculate_largest_rectangle(heights))


if __name__ == '__main__':
    unittest.main()
