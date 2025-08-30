"""Tests for reversals."""
import unittest

import reverse

class ReverseTestCase(unittest.TestCase):
    def testReverse(self):
        self.assertEqual(42, reverse.reverse_digits_bf(24))
        self.assertEqual(42, reverse.reverse_digits_bf(24))

        self.assertEqual(1132, reverse.reverse_digits(2311))
        self.assertEqual(-314, reverse.reverse_digits(-413))

if __name__ == '__main__':
    unittest.main()
