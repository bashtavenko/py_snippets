"""Flip the color of matrix."""

import collections

# Vertex is represented by Coordinate object
Coordinate = collections.namedtuple("Coordinate", ("x", "y"))


# We don't need marked set because color serves its purpose.


def flip_color_bfs(x, y, a):
    color = a[x][y]
    q = collections.deque([Coordinate(x, y)])
    a[x][y] = 1 - a[x][y]  # Flips
    while q:
        x, y = q.popleft()
        for x_offset, y_offset in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_x, next_y = x + x_offset, y + y_offset
            if (
                0 <= next_x < len(a)
                and 0 <= next_y < len(a[next_x])
                and a[next_x][next_y]==color
            ):  # This is sort of marked check
                a[next_x][next_y] = 1 - a[next_x][next_y]  # Flip
                q.append(Coordinate(next_x, next_y))


def run_dfs(c, a, color):
    """
    DFS version
    Args:
        c: coordinate
        a: array
        color: 0 or 1 for color
    """
    a[c.x][c.y] = 1 - a[c.x][c.y]  # Flips / marks
    for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
        next_x, next_y = c.x + x, c.y + y
        if (
            0 <= next_x < len(a)
            and 0 <= next_y < len(a[next_x])
            and a[next_x][next_y]==color
        ):
            run_dfs(Coordinate(next_x, next_y), a, color)


def flip_color_dfs(x, y, a):
    color = a[x][y]
    run_dfs(Coordinate(x, y), a, color)
