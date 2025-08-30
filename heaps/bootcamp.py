"""Heaps bootcamp.

https://hg.python.org/cpython/file/2.7/Lib/heapq.py

Heap in Python is not a data structure but a function that
mutates a list with
 - heapify (set up)
 - heappush (add)
 - heappop (delete)
 - heappushpop (add / delete)
 - nlargest, nsmallest (sort)
 - h[0] to get one element

There is no max heap.
"""

import heapq
import itertools


def top_k(k, stream):
    """
    Returns the longest k strings in the stream
    Returning the longest string requires min_heap and vice versa
    In the array it needs to be max_heap.
    """
    # islice: return iterator of k elements and stops at k
    # Make a list of (len, string) tuples
    # Grab first chunk and establish heap size.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]

    # Transform list into a heap, meaning rearrange item positions in min_heap
    heapq.heapify(min_heap)

    # Continue until the end of the stream, the steam is at k-the element
    # Here we discard the smallest while adding new.
    for next_string in stream:
        # Returns SMALLEST Item which we discard
        heapq.heappushpop(min_heap, (len(next_string), next_string))

    # What's left is the largest k elements, but the largest is not
    # the first. We need to sort which is not a problem because n is small
    return [p[1] for p in heapq.nsmallest(k, min_heap)]
