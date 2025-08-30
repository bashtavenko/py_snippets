"""Finds points of equilibrium in an array of integers.

   Meaning index of an element such as sum of elements to its left equals sum
   of elements to its rights.
"""


def find_bf(a):
    """Brute force."""
    for i in range(len(a)):
        sum_left, sum_right = 0, 0
        for j in range(0, i):
            sum_left += a[j]
        for k in range(i + 1, len(a)):
            sum_right += a[k]
        if sum_left == sum_right:
            break
    return i


def find_bf2(a):
    """Brute force improved, O(n)"""
    for i in range(len(a)):
        sum_left = sum(a[:i])
        sum_right = sum(a[i + 1 :])
        if sum_left == sum_right:
            break
    return i


def find_on(a):
    """O(n) time, same idea

    Walk one time and accumulate one sum while simultaneously reducing right
    sum by current element.
    """
    current_sum = sum(a)
    left_sum = 0
    for i in range(len(a)):
        current_sum -= a[i]
        if left_sum == current_sum:
            break
        left_sum += a[i]

    return i
