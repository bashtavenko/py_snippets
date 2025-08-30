"""24.2 Find the missing positive entry.

[3, 5, 4, -1, 5, 1, -1] => 2

Brute force: hash table, loop through numbers 1...n and see which a missing
Better: use current array as hashtable. This is sort of counting sort, but
it destroys the input

3, 4, 0, 2
0, 4, 3, 2
0, 2, 3, 4
"""


def find_first_missing_positive(a):
    # Record which values are present
    for i in range(len(a)):
        while 1 <= a[i] <= len(a) and a[i] != a[a[i] - 1]:
            a[a[i] - 1, a[i]] = a[i], a[a[i] - 1]

    # second pass
    return next((i + 1 for i, a in enumerate(a) if a != i + 1), len(a) + 1)
