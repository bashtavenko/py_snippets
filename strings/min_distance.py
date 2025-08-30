"""Given an array of characters, find the shortest distance between an X and a Y."""

import sys


def find(a, x, y):
    """Finds the shortest distance between x and y."""
    min_distance = sys.maxint
    x_index, y_index = None, None
    for i, c in enumerate(a):
        if c==x:
            x_index = i
        if c==y:
            y_index = i

        if x_index and y_index:
            current_min = abs(x_index - y_index)
            min_distance = min(current_min, min_distance)

    return -1 if min_distance==sys.maxint else min_distance


def find_with_list(x_list, y_list):
    """finds the shortest distance between x and y when given coordinates."""
    min_distance = sys.maxint
    y_list = sorted(y_list)
    for x in x_list:
        first_greater_y_index = find_first_greater_index(y_list, x)
        y = y_list[first_greater_y_index]
        current_min = abs(x - y)
        min_distance = min(current_min, min_distance)

        if first_greater_y_index > 0:
            y = y_list[first_greater_y_index - 1]
            current_min = abs(x - y)
            min_distance = min(current_min, min_distance)

    return -1 if min_distance==sys.maxint else min_distance


def find_first_greater_index(a, v):
    """Returns an index of the first element greater than v."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) / 2
        if a[mid] <= v:
            lo = mid + 1
        else:
            hi = mid
    return lo


def find_with_coordinates(x_coordinates, y_coordinates):
    """Finds the shortest distance."""


def find_2d(data):
    pass
