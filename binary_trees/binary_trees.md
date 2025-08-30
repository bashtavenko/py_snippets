# Reconstruct

1. Pre-order with markers. The simplest way
2. From in-order and post-order.

# LCA

No parent links - augment with Status, recurse to find number of common nodes
[code](binary_trees/lca.py), return status (num_nodes, ancestor)

With parent links - ascend [code](binary_trees/ca_with_parent.py), iterative.
Ascend from deeper than from both

# Get n-th

Based on in-order traversal

Nodes have child count
Select problem, can be recursive or iterative