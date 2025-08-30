"""18.1 Search maze."""

import collections

# BLACK - marked
WHITE, BLACK = range(2)

Coordinate = collections.namedtuple("Coordinate", ("y", "x"))


def search_maze(maze, start, end):
    def run_dfs(point):
        maze[point.x][point.y] = BLACK
        path.append(point)
        if point==end:
            return True

        for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_x, next_y = point.x + x, point.y + y
            if (
                0 <= next_x < len(maze)
                and 0 <= next_y < len(maze[next_x])
                and maze[next_x][next_y]==WHITE
            ):
                if run_dfs(Coordinate(next_x, next_y)):
                    return True

    path = []
    run_dfs(start)
    return path
