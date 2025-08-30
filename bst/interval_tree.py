"""Interval tree.
Cormen  14.3, p.348
Also: https://algs4.cs.princeton.edu/lectures/99GeometricSearch-2x2.pdf


            |----------|
         |---------|
|-----|
|-------------------------
0     3  5         8   10


      [5, 8]
        10
[0, 3]      [6, 10]
  3           10

Store three values in each node:
- Left endpoint (key)
- Right endpoint
- Max value

Number below is max value of the interval
[5, 8] has 10 because it has [6, 10]
Key is the left endpoint

This is for 1D range search, use KD tree for higher dimensions

Find all intervals that intersects the given query interval (lo, hi)

Insert: insert using lo, update max in each node on search path
"""

