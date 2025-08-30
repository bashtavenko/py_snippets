"""Similar to the original rod cutting by problem.

Maximize length of min sub array, essentially
find the narrowest trough

Prices: [1, 2, 3, 3, 2, 4, 4]
price changes in each segment

For three cuts, the minimum sub array has a length of 2
and a value of 5:

[1, 2, 3 | 3, 2 | 4, 4]
"""

PRICE = [1, 2, 3, 3, 2, 4, 4]


def cut_rod(length, k):
    """
    Returns longest sub array of minimum value.

    Args:
        length: length of array
        k: number of cuts

    Returns: value of longest sub array with minimum value.
    """
    if length < k:
        return 0
    if k == 1:
        return sum(PRICE[:length])  # up to this length

    max_so_far = 0
    for i in range(length - 1):
        cur = min(sum(PRICE[i:length]), cut_rod(i, k - 1))
    if cur > max_so_far:
        max_so_far = cur

    return max_so_far

def cut_rod_bottom_up(max_length, k):
    """TODO"""
    #
    # max_so_far = -sys.maxint
    # for length in range(1, max_length):
    #     for k in range(1, length + 1):
    #         cur = min(sum(PRICE[k:length], PRICE[length] + ...))
    #


if __name__ == '__main__':
    print (cut_rod(len(PRICE), 3))