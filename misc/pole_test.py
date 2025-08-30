"""Tests for pole."""

import unittest

import pole as m

WORDS = ["fuzzy", "apart", "steam", "times", "tires"]

"""
a: 3
f: 1..
"""


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.server = m.Server("tires")
        self.word = ["apple", "tales", "times", "steer" "tires"]

    def testGuess(self):
        self.assertEqual("-----", self.server.guess("fuzzy"))
        self.assertEqual("t-r--", self.server.guess("apart"))
        self.assertEqual("t--es", self.server.guess("steam"))
        self.assertEqual("ti-es", self.server.guess("times"))
        self.assertEqual("tires", self.server.guess("tires"))

    def testGuessDuplicate(self):
        server = m.Server("apart")
        # It could also be 'ap--'
        self.assertEqual("apa--", server.guess("apple"))


if __name__=="__main__":
    unittest.main()
