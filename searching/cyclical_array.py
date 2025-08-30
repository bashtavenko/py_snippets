"""11.3 Find the position of the smallest element in a cyclically sorted array.

Cyclical means it is possible to shift entities that array becomes
sorted.

378, 478, 550, 631, 103, 203, 220, 234, 279, 368

Answer [4] = 103
Essentially it's NOT a deep/peek finding because an array
is sorted but has one minimum.

Close to 1d nearest neighbour search
"""


def search_smallest(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > a[hi]:
            # Minium must be in a[mid + 1:hi + 1]
            lo = mid + 1
        else:  # a[mid] < a[hi]
            # Minimum cannot be in a[mid + 1:hi + 1]
            # so it must be in a[lo:mid + 1]
            hi = mid

    # Ends if lo == high
    return lo
