"""9.2 Test if binary tree is symetric
Check vertical line
"""


def check_symmetric(tree_left, tree_right):
    if not tree_left and not tree_right:
        return True
    elif tree_left and tree_right:
        return (
            tree_left.data == tree_right.data
            and check_symmetric(tree_left.left, tree_right.right)
            and check_symmetric(tree_left.right, tree_right.left)
        )
    return False
