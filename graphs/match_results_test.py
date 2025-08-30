"""Tests for match results."""

import unittest

import match_results as m


class MatchResultsTestCase(unittest.TestCase):
    def setUp(self):
        self.results = [
            m.MatchResult("a", "b"),
            m.MatchResult("a", "c"),
            m.MatchResult("b", "f"),
            m.MatchResult("b", "d"),
            m.MatchResult("b", "g"),
        ]

    def testCanBeat(self):
        self.assertTrue(m.can_team_a_beat_team_b(self.results, "a", "g"))
        self.assertFalse(m.can_team_a_beat_team_b(self.results, "c", "f"))

    def testCanBeat_v2(self):
        self.assertTrue(m.can_team_a_beat_team_b_v2(self.results, "a", "g"))
        self.assertFalse(m.can_team_a_beat_team_b_v2(self.results, "c", "f"))


if __name__=="__main__":
    unittest.main()
