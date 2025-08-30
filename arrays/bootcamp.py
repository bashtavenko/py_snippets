"""Partition an array into Even and Odd."""

import random


def even_odd(a):
    # Nothing to the left is odd and nothing to the right is even
    even = 0
    odd = len(a) - 1
    while even < odd:
        if a[even] % 2 == 0:
            even += 1
        else:
            a[even], a[odd] = a[odd], a[even]
            odd -= 1


def shuffle_in_place(a):
    for i in range(len(a)):
        next_index = random.randint(i, len(a) - 1)
        a[i], a[next_index] = a[next_index], a[i]


def shuffle_sort(a):
    # Idea - build a random array of the same length, sort it
    # [64, 1, 0, 8] => [0, 1, 8, 64]
    # p.index(s) for s in p_sorted => [2, 1, 3, 0]
    # n^3 to make sure that p are unique otherwise result may have dups
    p = [random.randint(i, pow(len(a), 3)) for i in range(len(a))]
    p_sorted = sorted(p)
    # index - returns element whose value is equal to s
    return [a[p.index(s)] for s in p_sorted]


def shuffle_sort_ex(a, p):
    return [a[p.index(s)] for s in sorted(p)]
