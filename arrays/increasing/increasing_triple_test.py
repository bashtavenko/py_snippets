"""Tests for increasing triple."""

import unittest

import increasing_triple


class IncreasingTrippleTestCase(unittest.TestCase):

    def testGetMaxTripplet(self):
        self.assertListEqual(
            [2, 6, 30],
            increasing_triple.get_max_tripplet(
                [45, 36, 32, 50, 33, 10, 5, 4, 3, 6, 2, 30, 1]
            ),
        )


if __name__ == "__main__":
    unittest.main()
