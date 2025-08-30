"""Return product of all items except current
[2, 1, 3] = [1 x 3, 2 x 3, 2 x 1] = [3, 6, 2]
[1, 2, 4, 3] = [24, 12, 6, 8]
[2, 3, 5, 4] = [60, 40, 24, 30]
"""

from functools import reduce
from operator import mul


def brute_force(data):
    """Double loop"""
    result = []
    for i in range(len(data)):
        product = 1
        for j in range(len(data)):
            if i == j:
                continue
            product *= data[j]
        result.append(product)
    return result


def with_divide(data):
    """Product all and then divide.
    reduce() - reduces iterable to a single value,
    [2, 1, 3] = 2 * 1 * 3 = 6, [6 / 2, 6 / 1, 6 / 3] = [3, 6, 2]
    """
    product_all = reduce(mul, data)
    return [product_all / x for x in data]


def both_ends(data):
    """
    [2, 3, 5, 4] = [60, 40, 24, 30]
    0: 1 | 3, 5, 4 = 60
    1: 2 | 5, 4 = 40
    2: 2, 3 | 4 => 24
    3: 2, 3, 5 | 1 => 30
    """
    result = []
    for i in range(len(data)):
        product_left = 1 if i == 0 else reduce(mul, data[:i])
        product_right = 1 if i == len(data) - 1 else reduce(mul, data[(i + 1) :])
        result.append(product_left * product_right)
    return result
