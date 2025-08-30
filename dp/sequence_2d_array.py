"""16.5 Find sequence in 2D array.

1 2 3
3 4 5
5 6 7

1, 3, 4, 6: Match
1, 2, 3, 4: No match
"""


def is_pattern_found(grid, p):
    def is_suffix_found(x, y, offset):
        if len(p) == offset:
            return True

        if (0 <= x < len(grid) and 0 <= y < len(grid[x]) and  # boundary check
            grid[x][y] == p[offset] and            # exists in grid
                (x, y, offset) not in cache and    # not seen before
                any(is_suffix_found(x + a, y + b, offset + 1) # has adjacent matches
                    for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)])):
            return True
        cache.add((x, y, offset)) # We've been here
        return False

    cache = set()
    return any(
        is_suffix_found(i, j, 0) for i in range(len(grid))
            for j in range(len(grid[i])))
