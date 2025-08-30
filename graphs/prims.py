import collections
import heapq

Edge = collections.namedtuple('Edge', ('v', 'w', 'weight'))

marked = set()
mst = collections.deque()
pq = []
heapq.heapify(pq)
graph = collections.defaultdict(set)


def run(graph, v):
    visit(v)

    while pq and len(mst) < len(graph):
        edge = pq.pop()
        mst.append(edge)
        if not edge.v in marked:
            visit(edge.v)
        if not edge.w in marked:
            visit(edge.w)


def visit(v):
    marked.add(v)
    for edge in graph[v]:
        if edge.other(v) not in marked:
            pq.heappushpop(pq, edge)

