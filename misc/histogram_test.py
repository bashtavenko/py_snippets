"""Tests for histogram bootcamp."""

import unittest

import histogram as m


class HistogramTestCase(unittest.TestCase):

    def testHistogram(self):
        people = [
            m.Person(1930, 1934),
            m.Person(1932, 1936),
            m.Person(1931, 1937),
            m.Person(1936, 1938),
        ]
        result = m.make_histogram(people)
        print(result)


if __name__=="__main__":
    unittest.main()
