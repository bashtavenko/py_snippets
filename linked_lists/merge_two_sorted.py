"""7.1 Merge two sorted lists.

"""
import bootcamp as b


def merge_two_sorted(l1, l2):
    head = tail = b.ListNode()

    while l1 and l2:
        if l1.data < l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next

    tail.next = l1 or l2

    return head.next


if __name__ == '__main__':
    list1 = b.ListNode(2, next = b.ListNode(5, next = b.ListNode(7)))
    list2 = b.ListNode(3, next = b.ListNode(11))
    result = merge_two_sorted(list1, list2)
    while result:
        print(result.data)
        result = result.next

