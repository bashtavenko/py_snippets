"""Tests for hashtable bootcamp."""

import unittest

import bootcamp as m


class BootcampTestCase(unittest.TestCase):

    def testAnagram(self):
        result = m.find_anagram(
            [
                "debitcard",
                "elvis",
                "silent",
                "badcredit",
                "lives",
                "freedom",
                "listen",
                "levis",
                "money",
            ]
        )
        print(result)


if __name__=="__main__":
    unittest.main()
