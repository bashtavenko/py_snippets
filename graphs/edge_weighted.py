"""Graphs basics."""
import collections

InputRecord = collections.namedtuple('InputRecord', ('src', 'dst', 'weight'))
Edge = collections.namedtuple('Edge', ('edge', 'weight'))


def build_graph(records):
    graph =  collections.defaultdict(set)
    for src, dst, weight in records:
        graph[src].add(Edge(dst, weight))
        graph[dst].add(Edge(src, weight)) # this may be 1 / weight or whatever
    return graph
