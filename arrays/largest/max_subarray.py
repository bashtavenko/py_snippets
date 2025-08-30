"""Maximum sub-array from Cormen.

Find contiguous nonempty array whose values have the largest sum.

We cannot simply sum from min to max elements
Day     0    1  2   3   4
Price   10  11  7   10  6
Change      1   -4  3   -4
Max is 3 after 2 and after 3. $7 is not the lowest and $10 is not the highest. This
is not buy-sell-stock once because of the negative values.

If there were only positive numbers, it would be just a matter of summing all numbers.

In the simplest case of [2, 3] it's a matter of picking up the maximum from left or right
but we need cross-sum (max sum from both sides).
Left: 2, Right: 3, Cross: 5
[2, 3, 7, -1]
Left: 5, Right: 6, Cross: 12 (Here cross is 12 because left is 5 and right is 7)
[7, -1] => 3
"""

import collections
import sys

Result = collections.namedtuple("Result", ("low", "high", "sum"))


def max_subarray(a):
    def find_max_crossing(low, mid, high):
        """Finds maximum subarray stretching from midpoint both ways"""
        left_sum, sum = -sys.maxsize, 0
        max_left, max_right = low, high
        for i in reversed(range(low, mid + 1)):
            sum += a[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum, sum = -sys.maxsize, 0
        for j in range(mid + 1, high + 1):  # Python stop is exclusive
            sum += a[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j

        return Result(max_left, max_right, left_sum + right_sum)

    def find_max_subarray(a, low, high):
        if low == high:
            return Result(low, high, a[low])

        mid = low + (high - low) // 2
        left_sum = find_max_subarray(a, low, mid)
        right_sum = find_max_subarray(a, mid + 1, high)
        cross_sum = find_max_crossing(low, mid, high)
        if left_sum.sum >= right_sum.sum and left_sum.sum >= cross_sum.sum:
            return Result(left_sum.low, left_sum.high, left_sum.sum)
        elif right_sum.sum >= left_sum.sum and right_sum.sum >= cross_sum.sum:
            return Result(right_sum.low, right_sum.high, right_sum.sum)
        else:
            return Result(cross_sum.low, cross_sum.high, cross_sum.sum)

    return find_max_subarray(a, 0, len(a) - 1)
