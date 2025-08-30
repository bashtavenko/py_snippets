"""Tests for histogram bootcamp."""
import unittest
from parameterized import parameterized

import brace_expansion as m

class BraceExpansionTestCase(unittest.TestCase):

    @parameterized.expand([
        ('_{a,b,c}{1,2}', '_a1 _a2 _b1 _b2 _c1 _c2')])
    def testBraceExpansion(self, src, expected):
      self.assertEqual(expected, m.expand(src))

if __name__ == '__main__':
    unittest.main()
