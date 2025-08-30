"""15.8 Generate binary trees."""

import collections

BinaryTreeNode = collections.namedtuple("BinaryTreeNode", ("data", "left", "right"))


def generate_trees(num_nodes):
    if num_nodes==0:
        return [None]

    result = []
    for num_left_nodes in range(num_nodes):  # Suppose those are left nodes
        num_right_nodes = num_nodes - 1 - num_left_nodes
        left_subtree = generate_trees(num_left_nodes)
        right_subtree = generate_trees(num_right_nodes)

        # Basically double for loop over left-right
        result += [
            BinaryTreeNode(0, left, right)
            for left in left_subtree
            for right in right_subtree
        ]

    return result


if __name__=="__main__":
    print(generate_trees(3))
