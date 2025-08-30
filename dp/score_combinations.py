"""16.1 Score combinations.

Given 2, 3 and 7 points,

1 way to get to 4:
2 + 2

2 ways to get to 7:
7
2 + 2 + 3

4 ways to get 12:
2 x 6
2 x 3 + 3 x 2
2 x 1 + 3 x 1 + 7 x 1
3 x 4

2D array to store the number of score combinations that result in a total of j
scores    0 1   2   3   4   5   6   7   ... 12
2         1 0   1   0   1   0   1   0       1  ( 2 x 6)
2,3       1 0   1   1   1   1   2   1       3
2,3,7     1 0   1   1   1   1   2   2       4
"""


def num_combinations(desired_score, scores):
    """Bottom up DP."""
    combinations = [[1] + [0] * desired_score for _ in scores]
    for i in range(len(scores)):  # scores = [2, 3, 7]
        for j in range(1, desired_score + 1):
            # without: one cell up
            without = combinations[i - 1][j] if i >= 1 else 0
            # with_score: this row to the left
            with_score = (combinations[i][j - scores[i]]
                          if j >= scores[i] else 0)

            combinations[i][j] = without + with_score
    return combinations[-1][-1]


