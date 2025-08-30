import unittest

import pangram as m


class PangramTestCase(unittest.TestCase):
    long_message = True

    def setUp(self):
        self.funcs = [m.is_pangram, m.is_pangram_set]

    def testPangram(self):
        phrase = "The quick brown fox jumps over the lazy dog"
        for f in self.funcs:
            self.assertTrue(f(phrase))


if __name__ == '__main__':
    unittest.main()
