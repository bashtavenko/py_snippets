"""Sequence overlapping intervals
            e8
          |----|
             e5
      |---------------|
          e1            e2
   |-----------|  |----------|
---------------------------------------------------------->
0  1  2  3  4  5  6   8      10 11     13 14  15    17

Should become:
          e1             e5           e8         e2
   |-----------|  |---------------| |----|  |----------|
---------------------------------------------------------->
0  1           5  6          10 11  12  13 14  15    17

e5 starts at 6 because it's best we could do, even though it wanted to start at 2
e8 also wanted to start at 4, but ended up being at 12 because it has to be after e5

"""
import collections

# This is input
Event = collections.namedtuple('Event', ('name', 'start', 'len'))

# Order events by start time
# name     start   len
# e1       1       4
# e5       2       6
# e8       3       2
# e2       6       4

def sequence_events(events):
    # Returns events sequenced according to their start time
    return sorted(events, key=lambda x: x.start)


