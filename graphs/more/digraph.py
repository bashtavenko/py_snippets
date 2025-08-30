"""Common graph infrastructure components."""

import collections
import heapq
import sys

Edge = collections.namedtuple('Edge', ('src', 'dst', 'weight'))
HeapItem = collections.namedtuple('HeapItem', ('weight', 'vertex'))


class Digraph:
    """Edge weighted digraph."""

    def __init__(self):
        self.graph = collections.defaultdict(set)
        self.min_heap = []
        self.dist_to = {}
        self.edge_to = {}
        heapq.heapify(self.min_heap)

    """Adds v -> w vertex."""
    def add_edge(self, v, w, weight):
        self.graph[v].add(Edge(v, w, weight))

    """Adds vertex without outbound edges."""
    def add_vertex(self, v):
        self.graph[v] = {}

    """Finds single-source shortest paths from s."""
    def run_classic_dijkstra(self, s):
        for v in self.graph.keys():
            self.dist_to[v] = sys.maxint
            self.edge_to[v] = {}
        self.dist_to[s] = 0
        heapq.heappush(self.min_heap, HeapItem(0, s))

        while self.min_heap:
            v = heapq.heappop(self.min_heap).vertex
            for e in self.graph[v]:
               self._relax(e)

    def _relax(self, e):
        v, w = e.src, e.dst
        if self.dist_to[w] > self.dist_to[v] + e.weight:
            # Keep invariant, this is the best so far.
            self.dist_to[w] = self.dist_to[v] + e.weight
            self.edge_to[w] = v

        # We need to see if w is in heap, and if it is then update it
        # This mimics index priority queue
        min_heap_index = next(iter(
          [i for i, item in enumerate(self.min_heap) if w == item.vertex]), -1)

        if min_heap_index >= 0:
            self.min_heap[min_heap_index] = HeapItem(self.dist_to[w], w)
            heapq.heapify(self.min_heap)
        else:
            heapq.heappush(self.min_heap, HeapItem(self.dist_to[w], w))
