"""Find the biggest consecutive segment within the budget.
 Returns the best sum, which is not greater than budget.
This is similar to largest_pair, the same idea.
"""


def biggest_segment(data, k):
    current_start = 0
    best_sum, current_sum = 0, 0
    for i, v in enumerate(data):
        current_sum += v
        while current_sum > k:
            current_sum -= data[current_start]
            current_start += 1
        best_sum = max(best_sum, current_sum)
    return best_sum
