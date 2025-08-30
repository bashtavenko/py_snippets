"""10.4 Compute k stars that are closest to Earth.

Since we need the smallest numbers, we need max_heap and keep popping
the biggest. What's left is smallest which we then need to sort.
"""

import heapq
import itertools


def find_closest(stream, k):
    max_heap = [-i for i in itertools.islice(stream, k)]
    heapq.heapify(max_heap)

    for item in stream:
        heapq.heappushpop(-item)

    # Sort what's left in the heap are the smallest, but they are
    # not sorted.
    return [s for s in heapq.nlargest(k, max_heap)]
