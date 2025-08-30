"""9.1 Test if binary tree is height-balanced.

For each node the difference between left and right subtree
is at most one.

Each node reports:
  a) if it's balanced;
  b) height of its children
So we either have to add those two attributes to each node, or recurse and
return them.
Do post order (left, right, than root)
"""

import collections


def is_balanced(tree):
    Status = collections.namedtuple("Status", ("balanced", "max_height"))

    def run(node):
        if not node:
            return Status(True, -1)

        left_result = run(node.left)
        if not left_result.balanced:
            return Status(False, 0)  # Height doesn't really matter

        right_result = run(node.right)
        if not right_result.balanced:
            return Status(False, 0)

        # Reached the bottom, begin to unwind (postorder).
        balanced_check = abs(left_result.max_height - right_result.max_height) <= 1
        max_height = max(left_result.max_height, right_result.max_height) + 1
        print(node.data, balanced_check, max_height)
        return Status(balanced_check, max_height)

    return run(tree).balanced
