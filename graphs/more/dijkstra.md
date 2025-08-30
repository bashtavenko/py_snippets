# Key ingredients
1. Edge object with src, dst, weight:
   ```
   Edge = collections.namedtuple('Edge', ('src', 'dst', 'weight'))
   ```
2. Index priority queue    
   Minimum heap with ability to directly update an item

3. Dictionary of distances to each vertex. Can be stopped when target
   vertex is reached.

4. Maintain tentative distances to all vertices

# Algorithm
 Initialize tentative distances to infinity except for the
first vertex, add first one to heap. Visit vertices in the order of their
distance to source vertex. 

**Invariant** - tentative distance is equal to the correct distance for
 settled nodes.

Visited nodes are relaxed.

Greedy chooses the "lightest" or "closest" vertex

#  Running time
O(V^2) where V is number of vertices with regular priority queue
but can be improved to O((V + E) lg V)

# Notes
Resembles BFS and Prim's for MST. Can be stopped when target vertex is
reached. 