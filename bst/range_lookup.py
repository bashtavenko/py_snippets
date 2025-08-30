"""14.12 Range lookup - find keys in range

Brute force: in-order traversal and get the keys.
Better - use BST property.

              50
          20         75
      12     21  65    80

15 - 30 => 20, 21

An interval search tree is more evolved and has max value of interval
"""
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def range_lookup(tree, lo, hi):
  def range_lookup_helper(tree):
    """Returns nodes in the given range"""
    if not tree :
      return

    if lo <= tree.data <= hi:
      result.append(tree.data)

    if tree.data >= lo:
      range_lookup_helper(tree.left)

    if tree.data <= hi:
      range_lookup_helper(tree.right)

  result = []
  range_lookup_helper(tree)
  return result
