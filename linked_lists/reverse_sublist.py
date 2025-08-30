"""7.2 Reverse list.

Actually reverse a portion of the list

11 -> 3 -> 5 -> 7 -> 2

2 - 4

11 -> 7 -> 5 -> 3 -> 2
"""

import bootcamp as b


def reverse_sublist(l, start, finish):
    head = sublist_head = b.ListNode(0, l)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next, sublist_head.next, temp)

    return head.next


if __name__ == '__main__':
    l = b.ListNode(
        11, next = b.ListNode(
            3, next = b.ListNode(
                5, next = b.ListNode(
                    7, next = b.ListNode(2)))))

    result = reverse_sublist(l, 2, 4)

    while result:
        print (result.data)
        result = result.next