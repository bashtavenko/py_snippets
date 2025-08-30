"""Tests for calendar."""
import unittest

import calendar as m

class CalendarTestCase(unittest.TestCase):

    def testFindMax(self):
        events = [
                m.Event(1, 5), m.Event(6, 10), m.Event(11, 13),
                m.Event(14, 15), m.Event(2, 7), m.Event(8, 9),
                m.Event(12, 15), m.Event(4, 5), m.Event(9, 17)]

        self.assertEqual(3, m.find_max_events(events))


if __name__ == '__main__':
    unittest.main()
