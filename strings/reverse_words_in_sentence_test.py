"""Tests for strings bootcamp."""
import unittest

import reverse_words_in_sentence as m


class ReverseTestCase(unittest.TestCase):
    def testReverse(self):
        s = list('Alice likes Bob')
        m.reverse(s)
        self.assertListEqual(list('Bob likes Alice'), s)


if __name__ == '__main__':
    unittest.main()
