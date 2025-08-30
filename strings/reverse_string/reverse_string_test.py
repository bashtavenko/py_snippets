import unittest

import reverse_string


class ReverseStringTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReverse(self):
        self.assertEqual(None, reverse_string.reverse(None))
        self.assertEqual(['f', 'o', 'o', ' ', 'b', 'a', 'r'],
                         reverse_string.reverse(
                             ['r', 'a', 'b', ' ', 'o', 'o', 'f']))


if __name__ == '__main__':
    unittest.main()
