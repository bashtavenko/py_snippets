"""
Calculate sum of all elements of the array that may include subarrays.
[1,[11,42,[8, 1], 4, [22,21]]] = 110
"""


def calc_sum(data):
    """Simple version with for loop."""
    result = 0
    for item in data:
        if isinstance(item, list):
            result += calc_sum(item)
        else:
            result += item

    return result


def cal_sum_recursive_basic(data):
    """Sum of sequence of numbers(no subsequences)"""

    def run(data, i):
        if i < 0:
            return 0
        else:
            return data[i] + run(data, i - 1)

    return run(data, len(data) - 1)


def cal_sum_recursive(data):
    """Version without 'for'"""

    def calc_sum(data, i):
        if i < 0:
            return 0

        current = data[i]
        if isinstance(current, list):
            current = calc_sum(current, len(current) - 1)

        return current + calc_sum(data, i - 1)

    return calc_sum(data, len(data) - 1)
