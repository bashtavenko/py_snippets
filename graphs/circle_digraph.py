"""Circles in digraph.
There can be cross-edges and back-edges which is why we cannot just
rely on marked vertices. 

The idea is to add a vertex to a set and remove it at the end. This
works because in case of cycle, there's going to be  a loop (well, cycle)
and that vertex will be detected.

This can be done with either stack or color-coding nodes with white, gray,
and black.

We need to run DFS from all vertices if graph is disconnected.
"""

import bootcamp as b


def detect_cycle(graph):
    marked = set()
    on_stack = set()
    has_cycle = set()

    def run_dfs(v):
        marked.add(v)
        on_stack.add(v)

        print(v)
        for w in graph[v]:
            if w not in marked:
                run_dfs(w)
            elif w in on_stack:
                has_cycle.add(w)
        on_stack.remove(v)

    for v in graph.keys():
        if v not in marked:
            run_dfs(v)

    return bool(has_cycle)


def detect_cycle_ex(graph):
    has_cycle = set()

    def run_dfs(v):
        v.color = b.GRAY
        print(v)
        for w in graph[v]:
            if w==b.WHITE:
                run_dfs(w)
            elif w==b.GRAY:
                has_cycle.add(w)
        w.color = b.BLACK

    for v in graph.keys():
        if v.color==b.WHITE:
            run_dfs(v)

    return bool(has_cycle)
