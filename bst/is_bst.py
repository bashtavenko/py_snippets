"""14.1 Check if BST.

No key in the left is greater

1. Meaning we can check every node to lo/hi and
start from -+ infinity
is subtree bst

2. Do inorder traversal which means all keys
should be in order

3. Run BFS in this way we can find it faster.
"""

import collections


def is_bst(tree, low=float("-inf"), high=float("inf")):
    if not tree:
        return True
    if not low <= tree.data <= high:
        return False
    return is_bst(tree.left, low, tree.data) and is_bst(tree.right, tree.data, high)


def is_bst_bfs(tree):
    QueueEntry = collections.namedtuple("QueueEntry", ("node", "low", "high"))
    bfs_queue = collections.deque([QueueEntry(tree, float("-inf"), float("inf"))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.low <= front.node.data <= front.high:
                return False
            bfs_queue.extend(
                [
                    QueueEntry(front.node.left, front.low, front.node.data),
                    QueueEntry(front.node.right, front.node.data, front.high),
                ]
            )
    return True
