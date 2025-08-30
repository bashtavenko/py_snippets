"""Tests for spikes."""

import unittest

import spikes as m


class SpikesTestCase(unittest.TestCase):

    def testSpikes(self):
        self.assertListEqual([], m.find_spikes([5, 4, 3, 2, 1]))
        self.assertListEqual([2], m.find_spikes([5, 4, 3, 8, 7, 6, 5]))
        self.assertListEqual([2, 2], m.find_spikes([2, 4, 1, 3]))


if __name__=="__main__":
    unittest.main()
