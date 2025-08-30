""" 14.3 Find the largest k-elements in BST.


We could do in-order traversal, put elements into queue and take k elements
but that would defeat the purpose of BST.


"""

import bootcamp as b


def find_k_largest(root, k):
    """Returns k-largest by using reversed in-order traversal.

    This is similar to k-th largest in linked list
    """

    def traverse(node):
        if node and len(result) < k:
            traverse(node.right)  # Reached the bottom, unwind
            # It is possible that there are more node in left
            if len(result) < k:
                result.append(node.data)
                traverse(node.left)  # Reversed in-order

    result = []
    traverse(root)
    return result


if __name__=="__main__":
    tree = b.BSTNode(
        20,
        left=b.BSTNode(10, left=b.BSTNode(8), right=b.BSTNode(12)),
        right=b.BSTNode(30, left=b.BSTNode(25), right=b.BSTNode(40)),
    )
    test = find_k_largest(tree, 3)
    print(test)
