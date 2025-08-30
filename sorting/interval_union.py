""" 13.7 Compute union of intervals.

"""

import collections

Endpoint = collections.namedtuple("Endpoint", ("is_closed", "va"))


class Interval:
    """Built-in sort uses __lt__ function."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.val!=other.left.val:
            return self.left.val < other.left.val
        return self.left.is_closed and not other.left.is_closed


def union_of_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    result = [intervals[0]]

    # .....
