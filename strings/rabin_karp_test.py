"""Tests for top queries."""
import unittest

import rabin_karp as m

class RabinKarpTestCase(unittest.TestCase):
    def testQueries_1(self):
        self.assertEqual(m.rabin_karp("describe", "es"), 1)
        self.assertEqual(m.rabin_karp("inahaystackneedleina",
                                      "needle"), 11)
        self.assertEqual(m.rabin_karp("describe", "foo"), -1)

if __name__ == '__main__':
    unittest.main()
