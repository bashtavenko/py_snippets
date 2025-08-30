""" 13.6 Merge intervals.

[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]
add [1, 8]
should become
[-4, -1], [0, 9], [11, 12], [14, 17]

Intervals are sorted, need to merge a new intervals to that list.

1. Simply add intervals before new one.

2. For the one that overlap:
if [a, b] and [c, d] overlap, union is
min(a, c), max(b, d)

3 Append the ones after

"""

import collections

Interval = collections.namedtuple("Interval", ("left", "right"))


def add_interval(intervals, new_interval):
    i, result = 0, []  # Need to keep a pointer all the way through

    # Append intervals before
    while i < len(intervals) and new_interval.left > intervals[i].right:
        result.append(intervals[i])
        i += 1

    # Now do merge
    while i < len(intervals) and new_interval.right >= intervals[i].left:
        new_interval = Interval(
            min(new_interval.left, intervals[i].left),
            max(new_interval.right, intervals[i].right),
        )
        i += 1

    # Process tail
    return result + [new_interval] + intervals[i:]


if __name__=="__main__":
    intervals = [
        Interval(-4, -1),
        Interval(0, 2),
        Interval(3, 6),
        Interval(7, 9),
        Interval(11, 12),
        Interval(14, 17),
    ]
    result = add_interval(intervals, Interval(1, 8))
    print(result)
