"""3 - sum.

(11, 2, 5, 7, 3) 21 = 3, 7, 11 or 5, 5, 11

"""

import bootcamp


def has_three_sum(A, t):
    A.sort()
    return any(bootcamp.has_two_sum(A, t - a) for a in A)
