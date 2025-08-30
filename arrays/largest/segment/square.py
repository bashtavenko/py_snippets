"""Largest square."""


def largest_square_n6(data, k):
    best_sum, square_sum = 0, 0
    n, m = len(data), len(data[0])
    for left in range(n):
        for right in range(n):
            for top in range(m):
                for bottom in range(m):
                    if is_square(left, right, top, bottom):
                        current_sum = compute_sum(data, left, right, top, bottom)
                        if k >= current_sum > best_sum:
                            best_sum = current_sum
    return best_sum


# For better than n6:
# Move square around and possibly grow. Do not recompute area on either move or grow
# Move 2 x 2, then 3 x 3 etc.


def is_square(left, right, top, bottom):
    return right - left == bottom - top and right - left > 0


def compute_sum(data, left, right, top, bottom):
    current_sum = 0
    for i in range(left, right + 1):
        for j in range(top, bottom + 1):
            current_sum += data[i][j]  # That is actually [row][column]
    return current_sum
