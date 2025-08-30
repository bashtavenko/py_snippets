"""Tests for overlapping intervals."""
import unittest

import overlapping_intervals as m

class IntervalsTestCase(unittest.TestCase):

    def testSequence(self):
        events = [
                m.Event('e1', 1, 4),
                m.Event('e2', 6, 4),
                m.Event('e5', 2, 6),
                m.Event('e8', 3, 2)]

        expected_events = [
                m.Event('e1', 1, 4),
                m.Event('e5', 2, 6),
                m.Event('e8', 3, 2),
                m.Event('e2', 6, 4)]

        result = m.sequence_events(events)
        self.assertListEqual(expected_events, result)


if __name__ == '__main__':
    unittest.main()
