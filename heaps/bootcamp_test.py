"""Tests for heaps bootcamp."""

import unittest

import bootcamp as m


class BootcampTestCase(unittest.TestCase):
    def testTopk(self):
        stream = ["a", "abce", "zxy", "de", "zanzibar", "foo", "bar", "adeeffd"]
        result = m.top_k(4, iter(stream))
        self.assertListEqual(["zxy", "abce", "adeeffd", "zanzibar"], result)


if __name__=="__main__":
    unittest.main()
