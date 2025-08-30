"""Find node in a tree.
"""
class Node(object):
  def __init__(self, value, name, children=None):
    self.value = value
    self.name = name
    self.children = children or []


def find_node(node,  value):
  if node.value == value:
    return node.name
  else:
    for child in node.children:
      result = find_node(child, value)
      if result:
        return result
    return None
