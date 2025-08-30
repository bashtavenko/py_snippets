"""Tests for mirror palindrome."""
import unittest

import string_mirror as m


class MirorTestCase(unittest.TestCase):

  def testMirror(self):
    self.assertTrue(m.is_mirror_palindrome('121'))
    self.assertTrue(m.is_mirror_palindrome('926'))
    self.assertTrue(m.is_mirror_palindrome('169691'))
    self.assertFalse(m.is_mirror_palindrome('373'))


if __name__ == '__main__':
  unittest.main()
