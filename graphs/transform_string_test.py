"""Tests for transform strings."""

import unittest

import transform_string as m


class TransformTestCase(unittest.TestCase):

    def setUp(self):
        self._d = {"bat", "cot", "dog", "dag", "dot", "cat"}

    def testTransform(self):
        self.assertEqual(3, m.transform_string(self._d, "cat", "dog"))

    def testTransform_missing(self):
        self.assertEqual(-1, m.transform_string(self._d, "cat", "foo"))


if __name__=="__main__":
    unittest.main()
