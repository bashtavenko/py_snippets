"""11.8 Find the k-th largest element of an unsorted array.

3, 2, 1, 5, 4
Largest: a[3],
third largest: a[0]
Assume entries are distinct.

Approaches:
  1. Brute force sort
  2. max-heap
  3. Keep random partitioning until we have pivot index in right position.
"""

import heapq
import operator
import random


def find_kth_heap(k, a):
    max_heap = [-v for v in a]
    heapq.heapify(max_heap)
    result = None
    for _ in range(k):
        result = heapq.heappop(max_heap)

    return -result


def find_kth_largest(k, a):
    def find_kth(comp):
        def make_partition(lo, hi, idx):
            """
            Tries to make a partition based on current state and array
            :param lo: start index
            :param hi: end index
            :param idx: current index
            :return: new index
            """
            pivot_value = a[idx]
            new_idx = lo
            a[idx], a[hi] = a[hi], a[idx]
            for i in range(lo, hi):
                if comp(a[i], pivot_value):
                    a[i], a[new_idx] = a[new_idx], a[i]
                    new_idx += 1
            a[hi], a[new_idx] = a[new_idx], a[hi]
            return new_idx

        left, right = 0, len(a) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = make_partition(left, right, pivot_idx)
            print(k, pivot_idx, new_pivot_idx, a)
            if new_pivot_idx == k - 1:
                return a[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1

    return find_kth(operator.gt)
