""" 14.5 Reconstruct BST.
We need PRE-ORDER traversal sequence. Note that this binary SEARCH
tree.

For BINARY trees we need both in-order and post-order or pre-order with markers.

      20
  10        30
8    12  25    40

20, 10, 8, 12, 30, 25, 40

Since it's PRE-ORDER, left subtree is whatever less than root,
right is whatever is greater.
Get 20, it's root, find index of first element greater than 20, that's 30
Get 10, 8, 12, that's left subtree. Get 30, 25, 40, that's right subtree
Recurse
This is only possible in BST and NOT a binary tree.
"""

import bootcamp


def rebuild_from_preorder(sequence):
    if not sequence:
        return None

    # Index of the RIGHT subtree:
    # i for i, a in enumerate(sequence) if a > sequence[0] - gets sequence
    # of indexes greater than first element of the array
    # next() - returns first element of the sequence
    # len(sequence) - if there are no elements in the sequence returns length
    transition_point = next(
        (i for i, a in enumerate(sequence) if a > sequence[0]), len(sequence)
    )

    # Now we know left and right subtrees.
    return bootcamp.BSTNode(
        sequence[0],
        rebuild_from_preorder(sequence[1:transition_point]),
        rebuild_from_preorder(sequence[transition_point:]),
    )
