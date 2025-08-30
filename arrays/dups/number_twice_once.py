"""In a sorted array where every number occurs twice, except one,
   find the number that occurs once.

   The number must be in the array.

   See duplicate_and_missing.py
"""


def find(a):
    """Step through every second item."""
    for i in range(1, len(a), 2):
        if a[i] != a[i - 1]:
            return a[i - 1]

    # Edge case with last one being single
    return a[len(a) - 1]


def find_xor(a):
    """x ^ x = 0  x ^ 0 = x"""
    s = 0
    for i in a:
        s ^= i
    return s


def find_binary_search(a):
    """Binary search to find single number in sorted array.

    1, 1, 3, 3, 5, 6, 6  mid = 3 (odd), 3 == 3 go right
    5, 6, 6              mid = 1 (odd), 6 <> 5 go left
    5

    2, 2, 3, 3, 4        mid = 2 (even), 3 == 3 go right
    4

    1, 2, 2, 3, 3        mid = 2 (even), 2 == 2 go left
    1, 2, 2              mid = 1 (odd),  1 <> 2 go left
    1
    """
    lo, high = 0, len(a) - 1

    while lo < high:
        mid = lo + (high - lo) // 2
        if mid % 2 == 0:
            # Even
            if a[mid] == a[mid + 1]:
                lo = mid + 2  # Go right
            else:
                high = mid  # Go left
        else:
            # Odd
            if a[mid] == a[mid - 1]:
                lo = mid + 1  # Go right
            else:
                high = mid - 1  # Go left

    return a[lo]
