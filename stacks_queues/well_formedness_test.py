"""Tests for well formed paranthesis."""
import unittest

import well_formedness as m


class WellFormednessTestCase(unittest.TestCase):
    def testIsWellFormed(self):
        self.assertTrue(m.is_well_formed('([]){()}'))
        self.assertTrue(m.is_well_formed('[()[]{()()}]'))
        self.assertFalse(m.is_well_formed('{)'))
        self.assertFalse(m.is_well_formed('[()[]{()()'))
        self.assertFalse(m.is_well_formed('(()][)'))
        self.assertTrue(m.is_well_formed('(()[])'))


if __name__ == '__main__':
    unittest.main()
