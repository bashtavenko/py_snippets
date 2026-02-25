import unittest

from arrays.dups import dups


class DupsTestCase(unittest.TestCase):
    long_message = True

    def testDeleteDupsBruteForce(self):
        a = [2, 3, 5, 5, 7, 11, 11, 11, 13]
        dups.delete_dups_brute_force(a)
        self.assertListEqual([2, 3, 5, 7, 11, 13, 0, 0, 0], a)

    def testDeleteDups(self):
        a = [2, 3, 5, 5, 7, 11, 11, 11, 13]
        dups.delete_dups(a)
        self.assertListEqual([2, 3, 5, 7, 11, 13, 0, 0, 0], a)


if __name__=="__main__":
    unittest.main()
