"""7.7 Remove k-last

Set two pointers with difference of k and then advance
both of them in tandem. When the first pointer reaches end,
the other pointer is at the right position.

It could also worked with recursion (find k-last)
"""
import bootcamp as b


def remove_k_last(l, k):
    dummy_head = b.ListNode(0, l)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next

    second.next = second.next.next
    return dummy_head.next


if __name__ == '__main__':
    l = b.ListNode(2, b.ListNode(5, b.ListNode(7, b.ListNode(9, b.ListNode(11)))))
    result = remove_k_last(l, 2)
    while result:
        print(result.data)
        result = result.next
