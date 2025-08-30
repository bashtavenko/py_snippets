"""Rod cutting."""

import sys
import collections

Result = collections.namedtuple('Result', ('Revenue', 'Path'))

PRICE = {
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17,
    7: 17,
    8: 20,
    9: 24,
    10: 30
}


def cut_rod(length):
    """Returns optimum revenue of cutting rod of given length.
    Returns price of whichever greater, current or l1 + l2 revenue
    """
    if length == 0:
        return 0
    revenue = -sys.maxint
    for n in range(1, length + 1):   # n is a cut point
        revenue = max(revenue, PRICE[n] + cut_rod(length - n))
    return revenue


def cut_rod_memoized(length, cache={}):
    """Same as cut_rod but with top-down memoization."""
    if length == 0:
        return 0
    elif length not in cache:
        revenue = -sys.maxint
        for n in range(1, length + 1):
            revenue = max(revenue, PRICE[n] + cut_rod_memoized (length - n, cache))
        cache[length] = revenue

    return cache[length]


def cut_rod_bottom_up(length):
    """Bottom-up non-recursive version."""
    cache = {0: 0}
    for j in range(1, length + 1):
        revenue = -sys.maxint
        for n in range(1, j + 1):
            revenue = max(revenue, PRICE[n] + cache[j - n])
        cache[n] = revenue

    return cache[length]


def cut_rod_bottom_up_path(length):
    """Bottom-up version with path."""
    cache = {0: 0}
    choices = {0: 0}
    for j in range(1, length + 1):
        revenue = -sys.maxint
        for n in range(1, j + 1):
            if revenue < PRICE[n] + cache[j - n]:
                revenue = PRICE[n] + cache[j - n]
                choices[j] = n
        cache[n] = revenue

    # Recover path
    path = []
    while length > 0:
        path.append(choices[length])
        length -= choices[length]

    return Result(revenue, path)
