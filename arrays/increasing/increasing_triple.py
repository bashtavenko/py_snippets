"""Given a sequence, return first increasing triple.

45, 36, 32, 50, 33, 10, 5, 4, 3, 6, 2, 30, 1 => 4, 6, 30

x, y, z
===============================================
(9223372036854775807, 9223372036854775807, 45)
(45, 9223372036854775807, 36)
(36, 9223372036854775807, 32)
(32, 9223372036854775807, 50)
(32, 50, 33)
(32, 33, 10)
(10, 33, 5)
(5, 33, 4)
(4, 33, 3)
(3, 33, 6)
(3, 6, 2)
(2, 6, 30)
Out[12]: [2, 6, 30]

This is similar to 2-sum, 3-sum, k-largest, etc

"""

import sys


def get_max_tripplet(a):
    x = sys.maxint
    y = sys.maxint
    for v in a:
        z = v
        print(x, y, z)
        if z > y:
            # Base case. If we only have to compare two numbers
            # that would be it.
            return [x, y, z]
        if z < x:
            x = z
        else:
            # z >= x and also z <= y
            # x <= y <= z
            y = z
    return []
