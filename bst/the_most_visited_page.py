""" 14.8 The most visited page problem.

[gattaaagtctat]
Four pages: acgt
a:4
t:3

Brute force:
1. Sort: aaaacggttt
2. Hash table (defaultdict, counter) and then k-largest
    12.5 k-most frequent queries (hash tables)
    a: 3
    c: 1
    g: 2
    t: 3
3. Better: Height-balanced BST
    Store page-to-visit count in each node

         3
      2    4

    Store map in a hash table
    3: a
    2: g
    Then find k-th largest

4. Priority queue - min_heap. I am not sure
"""
