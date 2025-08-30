"""7.10 Even-odd merge.

Nodes with even positions followed by node with odd positions

0    1    2    3    4
5 -> 1 -> 7 -> 4 -> 2
5 -> 7 -> 2 -> 1 -> 4
0    2    4    1    3
"""
import bootcamp as b


def even_odd_merge(l):
    if not l:
        return l

    even_dummy_head, odd_dummy_head = b.ListNode(0), b.ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0

    while l:
        tails[turn].next = l
        l = l.next
        tails[turn] = tails[turn].next
        turn ^= 1 # Flips between 0 and 1

    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next


if __name__ == '__main__':
    l = b.ListNode(5, b.ListNode(1, b.ListNode(7, b.ListNode(4, b.ListNode(2)))))
    result = even_odd_merge(l)
    while result:
        print(result.data)
        result = result.next

