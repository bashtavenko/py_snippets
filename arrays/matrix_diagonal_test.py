import unittest

import matrix_diagonal as m


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            [1, 2, 4, 3, 5, 7, 6, 8, 9],
            m.matrix_diagonally([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        )


if __name__=="__main__":
    unittest.main()
