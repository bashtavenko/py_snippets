""" 13.1 Find intersection of two sorted arrays.
Takes two sorted arrays and returns array with elements
present in both arrays. The input may have duplicates.

Example:
[2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
[5, 5, 6, 8, 8, 9, 10, 10]

[5, 6, 8]

Why not have two pointers move?
"""

import bisect


def intersect_arrays(a, b):
    def is_present(k):
        i = bisect.bisect_left(b, k)
        return i < len(b) and b[i]==k

    # This thing is to eliminate duplicates: if (i == 0 or x != a[i - 1])
    return [x for i, x in enumerate(a) if (i==0 or x!=a[i - 1]) and is_present(x)]
