"""Find common elements in two BST.

This is similar to merging two sorted arrays - pull from whoever is less
"""

def find_common(bst1, bst2):
    """Finds common elements."""
    # a_iter, b_iter = make_iter(bst1), make_iter(bst2)
    a_iter, b_iter = BstIterator(bst1), BstIterator(bst2)
    result = []

    first = next(a_iter, None)
    second = next(b_iter, None)

    # Core logic is the same regardless of making iterators
    while first is not None and second is not None:
        if first == second:
            result.append(first)
            first = next(a_iter, None)
            second = next(b_iter, None)
        elif first < second:
            first = next(a_iter, None)
        else:
            second = next(b_iter, None)

    return result

def make_iter(bst):
    """Brute force method of dumping tree into iterator."""
    def dump_in_order(node, result):
        if node:
            dump_in_order(node.left, result)
            result.append(node.data) # At the bottom
            dump_in_order(node.right, result)

    result = []
    dump_in_order(bst, result)
    return iter(result)


class BstIterator():
    """Better solution with iterable."""
    def __init__(self, root):
        self.node = root
        self.node_stack = []

    def __iter__(self):
        return self;

    def next(self):
        if not self.node_stack and not self.node:
            raise StopIteration()

        while self.node: # Keep going left until bottom
            self.node_stack.append(self.node)
            self.node = self.node.left

        self.node = self.node_stack.pop()
        data = self.node.data
        self.node = self.node.right
        return data
