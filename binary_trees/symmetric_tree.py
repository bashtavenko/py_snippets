"""9.2 Write a program that checks that binary tree is symmetric.

Meaning that corresponding nodes have the same values, but structurally the trees
are the same.
"""


def check_symmetric(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif tree1 and tree2:
        return (tree1.data == tree2.data and
                check_symmetric(tree1.left, tree2.right) and
                check_symmetric(tree1.right, tree2.left))

    # One subtree is empty, another is not
    return False
