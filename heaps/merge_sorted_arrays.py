""" 10.1 Merge sorted arrays."""

import heapq


def merge_sorted_arrays(sorted_arrays):
    # Build a list of iterators for each input array
    # What's cool in iterator approach is that
    # 1. We don't want names for each array, just use indexes;
    # 2. Don't worry about bounds, just do next(it, None)
    # If we had separate arrays a1, a2, a3, it could simply be
    # sorted_arrays_iters = [iter(a1), iter(a2), iter(a3)]
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Put first element from each iterator into min heap (heads)
    # For each element we need to know an array index it came from.
    min_heap = []
    for index, it in enumerate(sorted_arrays_iters):
        value = next(it, None)
        if value is not None:
            heapq.heappush(min_heap, (value, index))

    # The meat of it - iterate over all arrays (iterators) while
    # using heap to find the smallest.
    # The whole point of having heap is to find minimum element and its
    # index efficiently, that is O(log(n)) as opposed to O(n)
    # If we were to merge two arrays, it could simply be if-statement.
    # If number of arrays > 2, we would need linear search twice
    # once to find minimum element and second time to find index it came from.
    out = []
    while min_heap:
        smallest_entry, smallest_array_index = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_index]
        out.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element:
            heapq.heappush(min_heap, (next_element, smallest_array_index))

    return out
