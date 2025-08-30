"""Linked lists basics."""


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def insert_after(node, new_node):
    new_node.next = node.next  # double-linked
    node.next = new_node


def search_list(l, key):
    while l and l.data != key:
        l = l.next
    return l


def delete_after(node):
    node.next = node.next.next


def print_in_reverse(n):
    if not n:
        return

    print_in_reverse(n.next)

    # Reached the bottom stack begins to unwind
    # print n.data


def find_n_to_last(node, n):
    """Returns nth to last element from the linked list."""

    def find_n_to_last_helper(node, n, count):
        if not node:
            return None

        result = find_n_to_last_helper(node.next, n, count)
        # Reached the bottom of recursion (last node). It will never go higher.
        if count[0] == n:
            # This works but since we found the node, there is no point to keep
            # checking while unwinding stack, result will no longer be set and
            # the same result returned. So this essential sets result once.
            result = node.data

        count[0] += 1
        return result

    # Since there are no "pass by reference" in Python we wrap counter into a
    # mutable type.
    count = [0]
    return find_n_to_last_helper(node, n, count)
