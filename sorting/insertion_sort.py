"""Insertion sort."""


def insertion_sort(a):
    """Classical insertion sort.

    Best: n-1, worst n^2 / 2
    """
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1