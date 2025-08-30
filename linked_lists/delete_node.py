"""7.6 Delete a node from a singly linked list."""


def delete_node(node_to_delete):
    """Delete just this node.

    The point is to delete successor, we cannot delete the node itself
    with singly linked list since we don't know its parent.
    10 -> 11 -> 12 -> 13
    """
    # If we are deleting 11, we're wiping out 12
    node_to_delete.data = node_to_delete.next.data # 10 -> 11(12) -> 12 -> 13
    node_to_delete.next = node_to_delete.next.next # 10 -> 12 -> 13


def delete_every_other_node(head):
    node = head
    while True:
        # If list is circular, we can delete current node and don't need to
        # worry about successor
        node.next = node.next.next
        node = node.next
        if node == head or node.next == head:
            break
