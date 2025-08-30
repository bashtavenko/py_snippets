import unittest

import all_except_current as m

CASE_1 = [2, 1, 3]
CASE_1_RESULT = [3, 6, 2]

CASE_2 = [1, 2, 4, 3]
CASE_2_RESULT = [24, 12, 6, 8]

CASE_3 = [2, 3, 5, 4]
CASE_3_RESULT = [60, 40, 24, 30]


class AllExceptCurrentTestCase(unittest.TestCase):

    def setUp(self):
        self.funcs = [m.brute_force, m.with_divide, m.both_ends]

    def testAll(self):
        for f in self.funcs:
            self.assertListEqual(f(CASE_1), CASE_1_RESULT)
            self.assertListEqual(f(CASE_2), CASE_2_RESULT)
            self.assertListEqual(f(CASE_3), CASE_3_RESULT)


if __name__ == "__main__":
    unittest.main()
