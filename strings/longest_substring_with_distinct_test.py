import unittest

import longest_substring_with_distinct as m


class SubstringTestCase(unittest.TestCase):
    def testLongest(self):
        self.assertEqual("bbbzzbb", m.find_longest("azxbbbzzbboppop", 2))

    def testAppend(self):
        self.assertEqual("a", m.append_character("", "a", 2))
        self.assertEqual("az", m.append_character("a", "z", 2))
        self.assertEqual("zx", m.append_character("az", "x", 2))
        self.assertEqual("xb", m.append_character("zx", "b", 2))
        self.assertEqual("xbb", m.append_character("xb", "b", 2))
        self.assertEqual("xbbb", m.append_character("xbb", "b", 2))
        self.assertEqual("bbbz", m.append_character("xbbb", "z", 2))
        self.assertEqual("bbbzz", m.append_character("bbbz", "z", 2))
        self.assertEqual("bbbzzb", m.append_character("bbbzz", "b", 2))
        self.assertEqual("bbbzzbb", m.append_character("bbbzzb", "b", 2))
        self.assertEqual("bbo", m.append_character("bbbzzbb", "o", 2))

    def testBasics(self):
        self.assertEqual({"b": 3, "p": 2, "z": 2}, m.find_longest_2("azxbbbzzbboppop"))


if __name__ == "__main__":
    unittest.main()
