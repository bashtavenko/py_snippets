"""Find max sum a path can collect.

This is similar to 16.3, but with sum.

[1,2]
[3,3]

Path 1->2->3 = 6
Path 1->3->3 = 7
"""


def max_sum(data):
    def run(x, y):
        if x == y == 0:
            return data[x][y]

        if ways[x][y] == 0:
            ways_top = 0 if x == 0 else run(x - 1, y)
            ways_left = 0 if y == 0 else run(x, y -1)
            ways[x][y] = max(ways_top, ways_left) + data[x][y]

        return ways[x][y]

    ways = [[0] * len(data) for _ in range(len(data))]
    return run(len(data) -1, len(data) -1)


if __name__ == '__main__':
    data = [[1, 2],
            [3, 3]]
    print (max_sum(data)) # 7

    data = [[1, 2, 7],
            [0, 2, 1],
            [8, 5, 1]]
    print (max_sum(data))  # 1 + 0 + 8 + 5 + 1
