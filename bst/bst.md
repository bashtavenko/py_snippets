# Reconstruct

**Pre-order**. Get index of the first element less than root recursively.
This is a brute force.

For **binary** trees we need:

* Both in-order and post-order or
* Pre-order with markers

# Get n-th

Nodes have child node count - select (rank) problem

In-order make sense for finding is BST and greater or less

No node count:

1. Reversed in-order
2. In-order + queue

# LCA

This is a lot simpler then binary tree because we could use node values lca.py
The gist is

1. Iterative from the root
2. As soon as we find `v1 <= tree.data < v2`, we found LCA, given (1)

# Successor(first greater) in BST

From top Current node
Requires root Works on a subtree
No parent links Need parent links (no other way of going up)
Less code More code, need get_min
log(n)              n

# Range lookup

Get only key in range otherwise go left or right.
