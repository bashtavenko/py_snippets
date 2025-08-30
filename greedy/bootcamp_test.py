import unittest

import bootcamp as m


class BootCampTestCase(unittest.TestCase):

    def testHasTwoSum(self):
        a = [-2, 1, 2, 4, 7, 11]
        self.assertTrue(m.has_two_sum(a, 6))
        self.assertTrue(m.has_two_sum(a, 5))
        self.assertTrue(m.has_two_sum(a, 0))
        self.assertTrue(m.has_two_sum(a, 13))
        self.assertFalse(m.has_two_sum(a, 25))

    def test_change(self):
        self.assertEqual(6, m.change_making(48))
        self.assertEqual(2, m.change_making(60))
        self.assertEqual(1, m.change_making(10))


if __name__=="__main__":
    unittest.main()
