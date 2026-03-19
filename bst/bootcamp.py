""" BST bootcamp.

BST libraries

sortedcontainers
bintrees (insert, discard, min_item, min_key, pop_min)

"""

import bintrees


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def search(node, value):
    """Returns a node with a given value or None."""
    if not node or node.data==value:
        return node

    return search(node.left, value) if value < node.data else search(node.right, value)

def search_closest(node, value, closest=None):
    """Returns the closest node to the given value."""
    if node is None:
        return closest

    if closest is None or abs(node.data - value) < abs(closest - value):
        closest = node.data

    if value < node.data:
        return search_closest(node.left, value, closest)
    elif value > node.data:
        return search_closest(node.right, value, closest)
    else:
        return node.data


def search_closest_iterative(node, value):
    """Returns the closest node to the given value."""
    closest = node.data

    while node:
        if abs(node.data - value) < abs(closest - value):
            closest = node.data

        if value < node.data:
            node = node.left
        elif value > node.data:
            node = node.right
        else:
            return node.data

    return closest


def search_iterative(node, value):
    """Iterative version of search."""
    while node and node.data!=value:
        node = node.left if value < node.data else node.right
    return node


def get_min(node):
    if not node.left:
        return node
    return get_min(node.left)


def get_min_iterative(node):
    while node.left:
        node = node.left
    return node


def iterative_inorder(node):
    node_stack = []
    while node_stack or node:
        if node:
            # Keep going left adding each new node to the stack
            # because we need to go back
            node_stack.append(node)
            node = node.left
        else:  # At the bottom, going up
            node = node_stack.pop()
            print(node.data)
            node = node.right


def find_successor(node):
    """Returns successor (first greater) of the given node. Requires parent links.

    This is different from finding a key than a given value. That would have been
    in-order walk.

    There is a simpler solution that does not require parent links - start from the top,
    keep first_greater_so_far and go left or right depending on the node.
    That alternative solution requires root of the tree whereas this one works on
    subtree.

    Case 1: Look down, has a right link
    Left link makes no sense, no bigger nodes should be there. We cannot simply take
    the first node to the right. It works in the simplest case,
          9
            10
    It does not work because to (10) still have a successor of 9
         9
             50
           10   55
    therefore we need min in that subtree
    Case 2: Look up, this node is in some other node left subtree.
    This is trickier because it can be a trivial case of
          9 -> 10
        5
    but can also be (13 -> 15), again only right link of parent matters
                        15
                   6         18
                      7
                         13
    Therefore we need to:
        a) either go following right links or
        b) first parent
    """
    if node.right:  # Case 1, go down
        return get_min(node.right)
    # Case 2, go up
    # TODO(sb): there is no parent
    next_up_node = node.parent
    while next_up_node and node==next_up_node.right:  # Stop at 6 above
        node = next_up_node
        next_up_node = next_up_node.parent
    return node


def run_bin_tree():
    t = bintrees.RBTree(
        [(5, "Alpha"), (2, "Bravo"), (7, "Charlie"), (3, "Delta"), (6, "Echo")]
    )

    print(t[2])
    print(t.min_item(), t.max_item())


if __name__=="__main__":
    print(run_bin_tree())
