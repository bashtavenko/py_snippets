import unittest

import word_guess as m


class WordGuessTestCase(unittest.TestCase):
    def testScore(self):
        self.assertEqual(
            "RYGRR", m.score_word(secret="CHALK", guess="BLAST"), "No repetitions"
        )
        self.assertNotEqual(
            "YRGGG",
            m.score_word(secret="STAIR", guess="AGAIN"),
            "Repetitions in guess are the problem",
        )
        self.assertNotEqual(
            "GGRYR",
            m.score_word(secret="VIVID", guess="VIEVE"),
            "Repetitions in secret are the problem",
        )
        self.assertNotEqual(
            "RYGRY",
            m.score_word(secret="CHEER", guess="GEESE"),
            "Repetitions in both secret and guess",
        )

    def testScoreWithRepetitions(self):
        self.assertEqual(
            "GGRYR", m.score_word_with_repetitions(secret="VIVID", guess="VIEVE")
        )
        self.assertEqual(
            "RRGYR", m.score_word_with_repetitions(secret="SIEVE", guess="CHEER")
        )
        self.assertEqual(
            "RYGRR",
            m.score_word_with_repetitions(secret="CHEER", guess="GEESE"),
            "Used more than once",
        )
        self.assertEqual(
            "RRGGR",
            m.score_word_with_repetitions(secret="STAIR", guess="AGAIN"),
            "Used more than once - 2",
        )
        self.assertEqual(
            "YRRYR",
            m.score_word_with_repetitions(secret="RAISE", guess="AGAIN"),
            "Used more than once - 3",
        )


if __name__=="__main__":
    unittest.main()
