"""9.3 Compute LCA.

If both nodes are in left subtree go left, if both are in the right, go right.
If one is on the left and another on the right, found.

  Trivial case, b,c = a
      a
    b   c

      a
    b    z
  e   f

 e, f = b
 b, z = a

Recurse and return status.
"""

import collections

# num_nodes is number of nodes in the given tree
Status = collections.namedtuple("Status", ("num_nodes", "ancestor"))


def find_lca(tree, node0, node1):
    def find_helper(node):
        """Returns Status for the given nodes."""
        if not node:
            return Status(0, None)

        left_result = find_helper(node.left)
        if left_result.num_nodes == 2:  # Both on the left
            return left_result

        right_result = find_helper(node.right)
        if left_result.num_nodes == 2:  # Both on the right
            return left_result

        num_nodes = (
            left_result.num_nodes + right_result.num_nodes + int(node in (node0, node1))
        )

        return Status(num_nodes, ancestor=node if num_nodes == 2 else None)

    return find_helper(tree).ancestor
