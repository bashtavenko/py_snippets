"""14.4 Compute the LCA in a BST.

This is a lot simpler because we could use node values.
                  10
        5                  12
   1       7                     17

(1, 17) => 10

The gist is:
1. Iterative from the root
2. As soon as we find "v1 <= tree.data < v2", then we found LCA
"""

import bootcamp as b


def find_lca(tree, v1, v2):
    while tree.data < v1 or tree.data > v2:
        # Keep searching since tree is outside [node0, node1]
        while tree.data < v1:
            tree = tree.right  # went too far left
        while tree.data > v2:
            tree = tree.left  # went too far right

    return tree


if __name__=="__main__":
    n1 = b.BSTNode(1)
    n7 = b.BSTNode(7)
    n5 = b.BSTNode(5, left=n1, right=n7)
    n17 = b.BSTNode(17)
    n12 = b.BSTNode(12)

    root = b.BSTNode(10, left=n5, right=n12)

    print(find_lca(root, 1, 5).data)
