"""19.5 Deadlock.

If T1 and T1 need to acquire locks L and M, and T1 first acquires L and then T2 acquires M
meaning that L amd M can be accessed out of order.
   T1 T2
L  x      T1 found L first and locked it. Now it cannot get lock on M
M     x   T2 found M first and locked it. Now it cannot get lock on L

Solution: access resources in order
"""

