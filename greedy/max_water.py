"""17.7 Compute the maximum water tapped.

[1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
4 - 16


Brute force is O(n^3), divide and conquer is O(n^2)

This is similar to invariants such as two-sum and others.
"""


def get_max_water(heights):
    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1  # Keep i, want to try another j
        else:
            i += 1  # Wanted to see higher i
    return max_water
