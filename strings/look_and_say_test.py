"""Tests for strings bootcamp."""
import unittest

import look_and_say as m


class LookAndSayTestCase(unittest.TestCase):
    def testLookAndSay(self):
        self.assertEqual('1', m.look_and_say(1))
        self.assertEqual('11', m.look_and_say(2))
        self.assertEqual('21', m.look_and_say(3))
        self.assertEqual('1211', m.look_and_say(4))
        self.assertEqual('111221', m.look_and_say(5))
        self.assertEqual('312211', m.look_and_say(6))
        self.assertEqual('13112221', m.look_and_say(7))

        self.assertEqual('13112221', m.look_and_say_groupby(7))


if __name__ == '__main__':
    unittest.main()
