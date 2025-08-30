"""Flatten an iterator of iterators.
"""


class Flattener:
  def __init__(self, container):
    self.container_ = container


  # __iter__ is used in 'for' and 'in' statements
  def __iter__(self):
    for subcontainer in self.container_:
      for elem in subcontainer:
        yield elem
