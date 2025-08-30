"""Pick max amount of gold from lockers so that no two adjacent lockers
are empty. Lockers are form circle.

10, 8, 7, 1, 8 => 17 (10 +7)
10 + 7 + 8 = won't work because 10 and 8 are ajacent

Odd / even won't work
8, 0, 8, 0, 0, 8, 0, 8, 1 => 32 (8 + 8 + 8 + 8)
1, 7, 2, 7, 3, 8 => 22 (7 + 7 + 8)

Greedy won't work:
7, 6, 0, 6, 0, 5 => 17 (6 + 6 + 5)
Greedy: 13 (7 + 6) because we cannot take first 6 and last 5
So basically, what is greater, n + n(2)  or n(1)
"""


def get_max_recursive_demo(bars):
    """This just a demo, ignores first - last constraint."""
    def get_max_r(n):
        if n > len(bars) - 1:
            return 0  # Out of bound

        # 10, 8, 7, 1, 8
        #     n + n2, n1
        # max(8 + 0, 0) => 8 (bottom of recursion)
        # max(1 + 0, 8) => 8
        # max(8 + 0, 0) => 8
        # max(7 + 8, 8) => 7
        # ....
        # max(10 + 15, 16) => 10
        n_1, n_2 = get_max_r(n + 1), get_max_r(n + 2)
        print ('max({} + {}), {}. Current sum: {}'.format(
            bars[n], n_2, n_1, max(bars[n] + n_2, n_1)))
        return max(bars[n] + n_2, n_1)

    return get_max_r(0)


def get_max_cached(bars, cache={}):
    def get_max_c(n):
        if n > len(bars) - 1:
            return 0  # Out of bound

        if n not in cache:
            n_1, n_2 = get_max_c(n + 1), get_max_c(n + 2)
            cache[n] = max(bars[n] + n_2, n_1)
        return cache[n]

    return get_max_c(0)


def get_max(bars):
    """
    10, 8, 7, 1, 8 => 17 (10 +7)
    10 + 7 + 8 = 25 shouldn't work because 10 and 8 are adjacent
    and we have two choices, either 10, 7 (include first) or
    8, 1(don't include first)
    """
    with_first = get_max_recursive_demo(bars[:-1])
    without_first = get_max_recursive_demo(bars[1:])
    return max(with_first, without_first)


def get_max2(bars):
    """
    10, 8, 7, 1, 8 => 17 (10 +7)
    10 + 7 + 8 = 25 shouldn't work because 10 and 8 are ajacent
    and we have two choices, either 10, 7 (include first) or
    8, 1(don't include first)
    """
    with_first = get_max_cached(bars[:-1])
    without_first = get_max_cached(bars[1:])
    return max(with_first, without_first)


