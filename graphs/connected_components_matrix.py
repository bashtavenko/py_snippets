"""Connected components in matrix.

This is similar to connected components in graph, but the graph is represented
by pixel in matrix.

Union-Find implementation is even simpler:
Loop through all pixels, get pixels around it and union if
- It's 0
- Pixel next to it is 0
"""

def get_components(matrix):
    def run_dfs(v, vertices):
        marked.add(v)
        vertices.add(v)
        for w in (0, 1), (0, -1), (1, 0), (-1, 0):
            new_x, new_y = v[0] + w[0], v[1] + w[1]
            if (0 <= new_x < n and 0 <= new_y < m and
                (new_x, new_y) not in marked and
                matrix[new_x][new_y] == 0):
                run_dfs((new_x, new_y), vertices)

    marked = set()
    components = []
    n, m = len(matrix), len(matrix[0])

    for v in [(i, j) for i in range(m) for j in range(n)]:
        if v not in marked and matrix[i][j] == 0:
            vertices = set()
            run_dfs(v, vertices)
            components.append(vertices)
    return components
