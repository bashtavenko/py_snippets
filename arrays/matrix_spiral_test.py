import unittest

import matrix_spiral as m


class MatrixTestCase(unittest.TestCase):
    def testOdd(self):
        a = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        result = m.matrix_in_spiral(a)
        self.assertListEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], result)

    def testEven(self):
        a = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16])
        result = m.matrix_in_spiral(a)
        self.assertListEqual(
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10], result
        )


if __name__=="__main__":
    unittest.main()
