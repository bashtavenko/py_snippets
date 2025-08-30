"""7.3 Test for cycles.

1. Hash table
2. Two-loop traversal
3. Fast-slow pointers
    advance fast by two and slow by two
    pointer can cross only if there is a cycle
"""


def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Find the start of the cycle
            print 'Cycle'
            cycle_iter = head
            for _ in range(cycle_len(slow)):
                cycle_iter = cycle_iter.nexrt
            it = head

            # Advance both
            while it is not cycle_iter:
                it = it.next
                cycle_iter = cycle_iter.next
            return it # Start of the cycle
        return None