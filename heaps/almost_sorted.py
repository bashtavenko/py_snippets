""" 10.3. Takes sequence of numbers where each element is at most k away.

Example: k = 2
3, -1, 2, 6, 4, 5, 8

We only need to look at k + 1 numbers. For example, if k = 1:
3, -1, 2 => -1 / 3, 2 # May not be sorted but the lowest will be first
3, 2, 6  =>  2 / 3, 6
3, 6, 4  =>  3 / 6, 4
6, 4, 5  =>  4 / 5, 6
5, 6, 8  =>  5 / 6, 8
[-1, 2, 3, 4, 5] + [6, 8]

Why heap with size + 1 - we pop once and no need to worry about the rest
of the elements, they will be in place after the minimum is popped.
"""

import heapq
import itertools


def sort_almost_sorted(a, k):
    # It's easier to work with iterable
    sequence = iter(a)

    # Get first batch
    # islice - iterator slice, don't want to use regular slice (a[:k]) because
    # we have an iterator already, because we need to continue after :k
    min_heap = [x for x in itertools.islice(sequence, k)]
    heapq.heapify(min_heap)

    out = []

    # Since this is a sequence, we resume
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        out.append(smallest)

    # Get remaining k elements because we added them initially
    while min_heap:
        smallest = heapq.heappop(min_heap)
        out.append(smallest)

    return out
