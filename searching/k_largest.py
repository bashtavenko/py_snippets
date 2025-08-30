"""11.8 Find the largest k-element of an unsorted array.

3, 2, 1, 5, 4
Largest: a[3],
third largest: a[0]
Assume entries are distinct.

Approaches:
  1. Brute force sort
  2. max-heap
  3. Keep partitioning until we have pivot index in right position.
     (Randomized select)
"""

import heapq
import random


def find_kth_heap(k, a):
    max_heap = [-v for v in a]
    heapq.heapify(max_heap)
    result = None
    for _ in range(k):
        result = heapq.heappop(max_heap)

    return -result


def find_kth_largest(k, a):
    """There's a better version in quick_sort."""

    def partition_around_pivot(lo, hi, index):
        pivot_value = a[index]
        new_index = lo
        a[index], a[hi] = a[hi], a[index]
        for i in range(lo, hi):
            if a[i] > pivot_value:
                a[i], a[new_index] = a[new_index], a[i]
                new_index += 1
        a[hi], a[new_index] = a[new_index], a[hi]
        return new_index

    # Binary search, essentially
    left, right = 0, len(a) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
        print(k, pivot_idx, new_pivot_idx, a)
        if new_pivot_idx == k - 1:
            return a[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1
