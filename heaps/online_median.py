"""10.5 Compute online median of online data."""
import heapq


def online_median(sequence):
    # Two heaps, one stores minimum and another one maximum
    min_heap = [] # Minimum we have seen so far with max extracted
    max_heap = [] # Maximum we have seen so far with min extracted
    result = []

    for x in sequence:
        current_max = -heapq.heappushpop(min_heap, x) # Extract max
        heapq.heappush(max_heap, current_max)

        # Want both heaps be the same size.
        if len(max_heap) > len(min_heap):
            # Extract min
            print (f'Out of whack: {min_heap}{max_heap}')
            current_min = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, current_min)

        print (x, current_max, min_heap, max_heap)

        result.append((0.5 * (min_heap[0] + (-max_heap[0]))
                       if len(min_heap) == len(max_heap) else min_heap[0]))

    return result
