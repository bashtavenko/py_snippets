## Graphs basics

Representing graph - collection.defaultdict(set)

Keeping marked vertexes:

* Option 1: set(). Vertexes can be primitive numbers
* Option 2: Node object with marked property or color to indicate undiscovered, discovered but
  not yet explored (on the edge) and discovered and explored

BFS - nice to pack coordinates into an object, but can work with a tuple

DFS  
Can be conventional for-loop or Pythonic map

# Boilerplate

DFS   
Stock

```python
  mark
for v in graph[s]:
    if v is not in marked:
        marked.add
        dfs
```

## Other

Max Flow / Min cut (Ford Fulkerson)

### MST

Spanning tree - connected sub-graph that include all vertices and has no cycles

Cut - partitioning of graph vertices into two non-empty sets
Crossing edge - connects two sub-graph
Given any cut, the crossing edge of min weight is in MST

- Prim's (greedy, ala Dijkstra) with PQ

- Kruskal's (cycles)