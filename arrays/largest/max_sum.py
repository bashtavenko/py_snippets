"""
Given an array of positive integers find two non-consecutive numbers with
the largest sum.

Similar to largest_pair
"""


def max_sum_o_square(data):
    current_max = 0
    for i in range(len(data)):
        for j in range (1, len(data)):
            if data[i] + data[j] > current_max and j - i > 1:
                current_max = data[i] + data[j]

    return current_max


def max_sum(data):
    # Find maximum element and its index
    max_item, max_item_index = 0, -1
    for i, v in enumerate(data):
        if v > max_item:
            max_item_index = i
            max_item = v

    # Find second element
    current_max = 0
    for i, v in enumerate(data):
        if v + max_item > current_max and abs((i - max_item_index)) > 1:
            current_max = v + max_item

    return current_max
