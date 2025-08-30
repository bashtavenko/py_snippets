from unittest import TestCase

import square as m


class LargestSquare(TestCase):
    def test_largest_square(self):
        a = (
            [1, 1, 2, 4, 5],
            [1, 4, 5, 3, 7],
            [2, 7, 1, 1, 1],
            [7, 1, 1, 1, 1],
            [5, 2, 1, 1, 4],
        )

        # one is [7]
        # 1, 1
        # 1, 4
        # one is [12]
        # 1, 2
        # 4, 5
        # another one is [12]
        # 1, 1, 1
        # 1, 1, 1
        # 1, 1, 4
        self.assertEqual(12, m.largest_square_n6(a, 12))
