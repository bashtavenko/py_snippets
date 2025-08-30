"""18.3 Compute enclosed regions.

Fill regions that cannot reach the boundary, i.e. fill all
in-land lakes.

Start at the edge and grow in-ward with BFS from W's.  Need BFS
and not DFS because need the closest path.
"""

import collections


def compute_regions(board):
    """Replaces all 'W' that cannot reach the boundary with 'B'."""
    n, m  = len(board), len(board[0])
    # This puts all cells into the queue, it may be better to add
    # just the boundary
    q = collections.deque(
        [(i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))] +
        [(i, j) for k in range(m) for i, j in ((0, k), (m - 1, k))]
    )

    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
            board[x][y] = 'T' # Found W that can not reach the boundary
            # extend() - fancy way of adding multiple from iterable
            q.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    # [:] - create new list
    # Clean up 'T' reverting them to the original W (these can reach)
    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]


if __name__ ==  '__main__':
    # Three in the middle are enclosed
    board1 = [['B', 'B', 'B', 'B'],
              ['W', 'B', 'W', 'B'],
              ['B', 'W', 'W', 'B'],
              ['B', 'B', 'B', 'B']]

    # No enclosed
    board2 = [['B', 'B', 'B', 'B'],
              ['W', 'B', 'B', 'B'],
              ['B', 'B', 'B', 'B'],
              ['B', 'B', 'B', 'B']]

    # Flipped three W in the middle because they cannot reach the boundary
    compute_regions(board1)
    print (board1)

    compute_regions(board2)
    print (board2) # No changes, all W can reach the boundary