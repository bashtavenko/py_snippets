"""8.7 Compute binary tree nodes in order of increasing depth.

                314
       6                 6
 271      561         2     271

28   0       3            1      28

[314, 6, 6, 271, 561, 2, 271, 28, 0, 3, 1, 28]
"""

import collections


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def binary_tree_queue(tree):
    """What's the point? BFS is much simpler."""
    result, curr_depth_nodes = [], collections.deque([tree])
    while curr_depth_nodes:
        next_depth_nodes, this_level = collections.deque([]), []
        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)
        curr_depth_nodes = next_depth_nodes

    return result


def bfs(tree):
    result = []
    marked = set()
    marked.add(tree)
    q = collections.deque([tree])
    while q:
        v = q.popleft()
        result.append(v.data)
        for v in [v.left, v.right]:
            if v and v not in marked:
                marked.add(v)
                q.append(v)

    return result


if __name__ == "__main__":
    tree = Node(
        314,
        Node(6, Node(271, Node(28), Node(0)), Node(561, right=Node(3))),
        Node(6, Node(2, right=Node(1)), Node(271, right=Node(28))),
    )
    print(binary_tree_queue(tree))
    print(bfs(tree))
