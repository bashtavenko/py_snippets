"""Tests for strings bootcamp."""

import unittest

import bootcamp as m


class BootcampTestCase(unittest.TestCase):
    def setUp(self):
        self.l = m.ListNode(10)
        self.n1 = m.ListNode(11)
        m.insert_after(self.l, self.n1)

        self.n2 = m.ListNode(12)
        m.insert_after(self.n1, self.n2)

    def testSearch(self):
        self.assertEqual(12, m.search_list(self.l, 12).data)

    def test_delete(self):
        m.delete_after(self.n1)
        self.assertIsNone(m.search_list(self.l, 12))

    def test_print_in_reverse(self):
        m.print_in_reverse(self.l)

    def test_find_n_to_last(self):
        self.assertEqual(11, m.find_n_to_last(self.l, 1))
        self.assertEqual(10, m.find_n_to_last(self.l, 2))
        self.assertEqual(None, m.find_n_to_last(self.l, 5))


if __name__ == "__main__":
    unittest.main()
