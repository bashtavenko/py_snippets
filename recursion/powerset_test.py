import unittest

import powerset as m


class PowersetTestCase(unittest.TestCase):

    def testPowerset(self):
        result = m.power_set_bits("abc")
        self.assertEqual(["", "a", "b", "ab", "c", "ac", "bc", "abc"], result)

        result = m.power_set_bits("12")
        self.assertEqual(["", "1", "2", "12"], result)

        result = m.generate_powerset("abc")
        self.assertEqual(["", "c", "b", "bc", "a", "ac", "ab", "abc"], result)


if __name__=="__main__":
    unittest.main()
