"""13.5 Determine the maximum number of events that take place concurrently.
             e8                      e9
          |----|           |------------------------|
             e5          e6              e7
      |---------------| |--|         |------]
          e1            e2         e3      e4
   |-----------|  |----------|  |------|  |---|
---------------------------------------------------------->
0  1           5  6          10 11     13 14  15    17

Maximum number of concurrent events is 3 (e1, e5, e8) or (e3, e7, e9) or (e4, e7, e9)

Convert intervals to points and then sort points ascending by x and is_start:
X  is_start
1  y
2  y
4  y
5  n
5  n
....
9  y  # If x is the same, start should come before finish
9  n

Then walk that sorted list of points and track counts.
"""
import collections

# This is input
Event = collections.namedtuple('Event', ('start', 'finish'))

# Internal Point structure
# In this example: (1, start), (2, start), (5, end), (9, start), (9, end)
Point = collections.namedtuple('Point', ('x', 'is_start'))


def find_max_events(events):
    # Build a list of points out of input list of events
    points = ([Point(event.start, True) for event in events] +
              [Point(event.finish, False) for event in events])

    points.sort(key=lambda e: (e.x, not e.is_start))

    max_num_concurrent, num_concurrent = 0, 0

    for point in points:
        if point.is_start:
            num_concurrent += 1
            max_num_concurrent = max(num_concurrent, max_num_concurrent)
        else:
            num_concurrent -= 1

    return max_num_concurrent
