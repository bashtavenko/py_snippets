"""Tests for linked list with some basic operations."""
import unittest

import bootcamp as b
import delete_node as m


class DeleteTestCase(unittest.TestCase):
    def setUp(self):
        self.l = _make_list([10, 11, 12, 13, 14, 15])

    def test_delete_node(self):
        n = _find_node(self.l, 11)
        m.delete_node(n)
        result = list(_convert_to_iter(self.l))
        self.assertItemsEqual([10, 12, 13, 14, 15], result)

    def test_delete_node_2(self):
        n = _find_node(self.l, 14)
        m.delete_node(n)
        result = list(_convert_to_iter(self.l))
        self.assertItemsEqual([10, 11, 12, 13, 15], result)

    def test_delete_every_other_node(self):
        l = _make_circular_list([10, 11, 12, 13, 14, 15, 16, 17, 18])
        m.delete_every_other_node(l)

def _convert_to_iter(root):
    node = root
    while node:
        yield node.data
        node = node.next

def _make_list(sequence):
    dummy_root = b.ListNode()
    node = dummy_root
    for item in sequence:
        node.next = b.ListNode(item)
        node = node.next
    return dummy_root.next

def _make_circular_list(sequence):
    dummy_root = b.ListNode()
    node = dummy_root
    for item in sequence:
        node.next = b.ListNode(item)
        node = node.next
    node.next = dummy_root.next
    return dummy_root.next

def _find_node(node, data):
    while node:
        if node.data == data:
            return node
        node = node.next
    return None


if __name__ == '__main__':
    unittest.main()
