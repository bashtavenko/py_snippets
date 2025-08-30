import unittest

import parity


class ParityTestCase(unittest.TestCase):

    def testParity(self):
        self.assertEqual(1, parity.brute_force_41(13))
        self.assertEqual(0, parity.brute_force_41(12))

        self.assertEqual(1, parity.brute_force(13))
        self.assertEqual(0, parity.brute_force(12))

        self.assertEqual(1, parity.parity(13))
        self.assertEqual(0, parity.parity(12))


if __name__ == "__main__":
    unittest.main()
