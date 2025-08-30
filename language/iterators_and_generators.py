"""Iterators and generators."""
# Iterable - it's just an object that implements __iter__(), __next()__().
#

import random


class RandomIncrement():
  def __init_(self, limit):
    self._offset = 0.0
    self._limit = limit

  def __iter__(self):
    # This is used in 'for' and 'in' statements
    return self

  def __next__(self):
    # Returns next or exception
    self._offset += random.random()
    if (self._offset > self._limit):
      raise StopIteration()
    return self._offset

  def increment_limit(self, increment_amount):
    self._limit += increment_amount


# Generator is an easy way to create iterators.
# Uses function call stack to remember position
# Every Generator is Iterator, but not reverse.
def random_iterator(limit):
  offset = 0
  while True:
    offset += random.random()
    if offset > limit:
      raise StopIteration()
    yield offset
