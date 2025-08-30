import unittest

import permutations as m


class PermutationsTestCase(unittest.TestCase):
    def testPermutations(self):
        result = m.perm_backtracking("abc")
        self.assertListEqual(["abc", "acb", "bac", "bca", "cba", "cab"], result)


if __name__=="__main__":
    unittest.main()
