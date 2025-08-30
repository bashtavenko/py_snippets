"""Reconstruct binary tree from in-order and post order traversals.
  1
2   3
I:    2, 1, 3
POST: 2, 3, 1

       1
  2        3
4    5   6   7
  8

I:    4, 8, 2, 5, 1, 6, 3, 7
POST: 8, 4, 5, 2, 6, 7, 3, 1

Must have BOTH In-order and post-order.
1. Find last element in post-order, that's root
2. Find matching element in in-order, these are left and right branches
3. Recurse

Since this is binary tree, we can't get away with just pre-order along since we don't
know if nodes are less or greater.

The only way to reconstruct binary tree from just pre-order is to store
pre-order marker a, b, None, None.
"""

import bootcamp


def construct_tree(in_order, post_order):
    def _build(start, end):
        if start==end:
            return None

        node = bootcamp.BinaryTreeNode(post_order.pop())
        index = in_order.index(node.data)
        node.right = _build(index + 1, end)
        node.left = _build(start, index)
        return node

    return _build(0, len(in_order))
