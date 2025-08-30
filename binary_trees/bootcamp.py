"""Binary trees bootcamp.py

     10
  8     20

In-order: 8, 10, 20
Pre-order: 10, 8, 20 (BEFORE / PRE)
Post-order: 8, 20, 10 (leaves then ROOT)
Reversed post-order: 20, 8, 10 (leaves right, left then ROOT)
"""


class BinaryTreeNode:

    def __init__(self, data=None, left=None, right=None,
                 parent=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.size = size


def traverse_preorder(node):
    if node:
        print ('Preorder:', node.data)
        traverse_preorder(node.left)
        traverse_preorder(node.right)

def traverse_inorder(node):
    if node:
        traverse_inorder(node.left)
        print ('Inorder', node.data)
        traverse_inorder(node.right)

def traverse_postorder(node):
    if node:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print ('Postorder', node.data)

