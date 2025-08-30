from unittest import TestCase

import segment as m


class SegmentTestCase(TestCase):
    def test_biggest_segment(self):
        self.assertEqual(4, m.biggest_segment([3, 1, 1, 2, 1, 1], 4))

    def test_biggest_segment_2(self):
        self.assertEqual(7, m.biggest_segment([3, 2, 3, 1, 4, 1, 1, 3], 7))

    def test_biggest_segment_allBelow(self):
        self.assertEqual(5, m.biggest_segment([3, 1, 1], 10))

    def test_biggest_segment_oneExceeds(self):
        self.assertEqual(6, m.biggest_segment([1, 10, 1, 5], 7))

    def test_biggest_segment_everyExceeds(self):
        self.assertEqual(0, m.biggest_segment([7, 8, 3, 2], 1))

    def test_biggest_segment_rightMost(self):
        self.assertEqual(10, m.biggest_segment([1, 2, 3, 4, 1], 10))

    def test_biggest_segment_oneHuge(self):
        self.assertEqual(1, m.biggest_segment([1, 10], 2))
