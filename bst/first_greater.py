"""14.2 Find the first key greater than a given value.

"""


def find_bf(tree, k):
    # In-order traversal.

    """
                43
          29           47
      23       37         53

    In-order: 23, 29, 37, 43, 47, 53
    This does not take into account that it is BST,
    just in-order traverse as it's a graph or binary tree.
    It is just an in-order walk with O(N).
    """
    if not tree:
        return None
    result = find_bf(tree.left, k)
    if result:  # We need to short-circuit, otherwise it will keep going
        return result
    if tree.data > k:
        return tree
    result = find_bf(tree.right, k)
    if result:
        return result

    return None


def find(tree, k):
    """Better approach.

    Use BST property, start from the top, keep first_so_far
    Iterative, just like binary search.
         37
     29   41
       31    43
          32
    """
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            # It does not mean going through right all the time
            # see above example of (41, 33)
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far
