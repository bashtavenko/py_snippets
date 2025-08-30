"""Broken binary tree."""
import collections

def find_broken_edge(node):
  marked = set()

  def dfs(s):
    if s is None: return
    print (s.data)
    marked.add(s)

    for v in [s.left, s.right]:
      if v not in marked:
        dfs(v)
      else:
        print ('Broken edge: {} => {}'.format(s.data,v.data))

  dfs(node)
