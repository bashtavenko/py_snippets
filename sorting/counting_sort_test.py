"""Tests for Counting Sort."""
import unittest

import counting_sort as m

class CountingSortTestCase(unittest.TestCase):

    def testSort(self):
        a = [2, 5, 3, 0, 2, 3, 0, 3]
        expected = [0, 0, 2, 2, 3, 3, 3, 5]
        # result = m.counting_sort_classic(a, 6)
        result = m.counting_sort(a, 6)
        self.assertEqual(result, expected)

    def testRadixSort(self):
        a = [329,
             457,
             657,
             839,
             436,
             720,
             355]
        expected = [329,
                    355,
                    436,
                    457,
                    657,
                    720,
                    839]
        result = m.radix_sort(a, 3, 10)
        self.assertEqual(expected, result)

    def testCountingOnPosition(self):
        a = [329,
             457,
             657,
             839,
             436,
             720,
             355]
        expected = [720,
                    355,
                    436,
                    457,
                    657,
                    329,
                    839]
        self.assertEqual(expected, m.counting_sort_on_digit(a, 0, 10))


if __name__ == '__main__':
    unittest.main()
