"""Connected components."""
import collections

InputEdge = collections.namedtuple('InputEdge', ('v', 'w'))


def build_graph(edges):
    graph = collections.defaultdict(set)
    for v, w in edges:
        graph[v].add(w)
        graph[w].add(v)
    return graph


def get_components(graph):
    def run_dfs(v, vertices):
        marked.add(v)
        vertices.add(v)
        for w in graph[v]:
            if w not in marked:
                run_dfs(w, vertices)

    marked = set()
    components = []
    for v in graph.keys():
        if v not in marked:
            vertices = set()
            run_dfs(v, vertices)
            components.append(vertices)
    return components
