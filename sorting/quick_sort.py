"""Quick sort."""
import random


def randomized_partition(a, lo, hi):
    """Randomized version of partitioning."""
    i = random.randint(lo, hi)
    a[i], a[hi] = a[hi], a[i]
    return partition(a, lo, hi)


def partition (a, lo, hi):
    """
    Partitions array by walking it left to right and keeping two invariants
    1. Everything left to i is less than pivot (but not necessarily sorted)
    2. Everything between i and j is greater or equal than pivot (but not necessarily sorted)
    Everything right to j has not been seen yet.
    Uses a[hi] as pivot
    Args:
        a: array
        lo: left index
        hi: right index
    Returns:
        Pivot position
    """
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i] # Restore invariant
            i += 1
    a[i], a[hi] = a[hi], a[i] # Move pivot where it should be
    return i


def randomized_quick_sort(a, lo, hi):
    if lo < hi:
        p = randomized_partition(a, lo, hi)
        randomized_quick_sort(a, lo, p - 1)
        randomized_quick_sort(a, p + 1, hi)


def quick_sort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quick_sort(a, lo, p - 1)
        quick_sort(a, p + 1, hi)


def select(a, k):
    return randomized_select(a, 0, len(a) - 1, k)


def randomized_select(a, lo, hi, k):
    """Returns the k-smallest element in the list.

    Args:
        a: iterable of int
        lo: lowest index
        hi: highest index
        k: order of the element (1st, 2nd, 3rd, etc)

    Returns:
        Value of the k-smallest from a
    """
    if lo > hi:
        return a[lo]
    p = randomized_partition(a, lo, hi)
    if p == k - 1:
        return a[p] # Pivot is the answer
    elif p > k - 1:
        return randomized_select(a, lo, hi - 1, k)
    else:
        return randomized_select(a, p + 1, hi, k)