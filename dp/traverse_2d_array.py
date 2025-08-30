"""16.3 Count the number of ways to traverse a 2D array.

Start at top left corner and getting to the bottom right corner.  All moves
rights and down.

The number of ways to get to the bottom-right entry is the number of ways to
get to the entry immediately above it, plus the number of ways to the entry
immediately to its left. If somebody gave me those two numbers on the silver
platter.

(i, j) = (i - 1, j) + (i, j - 1)

    1 1 1  1  1
    1 2 3  4  5
    1 3 6  10 15
    1 4 10 20 35
    1 5 15 35 70

We just need to cache the results.

0 1 1
1 2 3
1 3 6
"""


def num_of_ways(n):
    def run(x, y):
        if x == y == 0:
            return 1

        if ways[x][y] == 0:
            ways_top = 0 if x == 0 else run(x - 1, y)
            ways_left = 0 if y == 0 else run(x, y - 1)
            ways[x][y] = ways_top + ways_left
        return ways[x][y]

    ways = [[0] * n for _ in range(n)]
    return run(n - 1, n - 1)


if __name__ == "__main__":
    w = num_of_ways(3)
    print(w)
