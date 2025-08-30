## Sequence overlapping intervals
Simply sort interval by their start time

## Find max number of concurrent intervals
Concurrent - interval run at the same time (but may not end at the same time)
Convert intervals to points (x, is_start), walk points and count concurrent

## Merge one interval into existing ones
```
if [a, b] and [c, d] overlap, union is min(a, c), max(b, d)
```
Just left to right with three while loop keeping pointer throughout

## Interval tree - search interval intersection
Search for any one interval that intersects query (lo, hi)

