"""Given two nodes in binary tree, find LCA.
      a
   b     e
 c  d

c, d => b
c, e => a
"""


def find_lca(n0, n1):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    d0, d1 = get_depth(n0), get_depth(n1)

    # Start from deeper node
    if d1 > d0:
        n0, n1 = n1, n0

    # Ascend from deeper to level up
    diff = abs(d0 - d1)
    while diff:
        n0 = n0.parent
        diff -= 1

    # Now ascend from both
    while n0 is not n1:
        n0, n1 = n0.parent, n1.parent

    return n0
