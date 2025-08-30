"""Max sum of two numbers or the largest pair.
"""

import sys


def get_largest_pair(a):
    x, y = -sys.maxint, -sys.maxint
    # Move through while maintaining invariant of x >= y
    for v in a:
        if v > x:
            # Invariant is x >= y
            # If v > x, then at least y should be x
            y = x
            x = v  # The highest x
        elif v > y:  # We know that x > y and so replace only y
            y = v

    if x == y or x == -sys.maxint or y == -sys.maxint:
        return ()
    else:
        return x, y
