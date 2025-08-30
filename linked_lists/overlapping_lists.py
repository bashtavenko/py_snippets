"""7.4 Test for overlapping lists.

No cycles
"""
import bootcamp as b


def test_for_overlapping(l1, l2):
    def find_length(l):
        length = 0
        while l:
            length += 1
            l = l.next
        return  length

    l1_len, l2_len = find_length(l1), find_length(l2)

    if l1_len > l2_len:
        l1, l2 = l2, l1

    # Advance the longer list to the point where they are the same
    for _ in range(abs(l1_len - l2_len)):
        l2 = l2.next

    while l1 and l2 and l1 is not l2:
        l1, l2 = l1.next, l2.next

    return l1


if __name__ == '__main__':
   shared = b.ListNode(10, next = b.ListNode(11, next = b.ListNode(12)))
   l1 = b.ListNode(1, next = b.ListNode(2, next = shared))
   l2 = b.ListNode(3, next = shared)
   print test_for_overlapping(l1, l2).data
