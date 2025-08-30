""" 9.13 Reconstruct binary tree from pre-order with markers.
  1
2   3

1, 2, None, None, 3, None, None

This is the simplest way to restore binary tree. More complicated way is by
using in-order and post-order traversals.
"""

import bootcamp


def reconstruct(preorder):
    def reconstruct_helper(preorder_iter):
        node = next(preorder_iter)
        if node is None:
            return None
        left_subtree = reconstruct_helper(preorder_iter)
        right_subtree = reconstruct_helper(preorder_iter)
        return bootcamp.BinaryTreeNode(node, left_subtree, right_subtree)

    return reconstruct_helper(iter(preorder))
