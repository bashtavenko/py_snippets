"""Get n-th node based on in-order traversal. Nodes have child count.

               a (6)
           b(4)         f(1)
       c(1)  d(2)
               e (1)
0 1 2 3 4 5
c b d e a f

get(2) => d (two nodes to the left in in-order traversal)
get(3) => e

This is "select" problem.

For example, if left subtree has seven nodes, the tenth node cannot be in left
subtree.
"""

class Node:
  """Binary tree or binary search tree node."""
  def __init__(self, data=None, left=None, right=None,
               size=None):
      self.data = data
      self.left = left
      self.right = right
      self.size = size


def select(node, k):
  """Returns node with k-th position in in-order traversal."""
  if not node:
    return None

  t = node.left.size if node.left else 0  # How many nodes are to the left?
  if t > k: # More than one need, keep going left
    return select(node.left, k)
  elif t < k:
    return select(node.right, k - t - 1)  # k == nodes in right subtree
  else:
    return node  # t == k(k may be reduced from original one)


def select_iterative(node, k):
  """Iterative version of select."""
  while node:
    t = node.left.size if node.left else 0  # How many nodes are to the left?
    if t > k: # There's more there, keep on going
      node = node.left
    elif t < k:
      k -= t + 1
      node = node.right
    else:
      return node
  return None
