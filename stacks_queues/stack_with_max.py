"""8.1 Stack with max.
"""
import collections


class Stack:
    # Store each element with maximum stored at or below that entry.
    ElementWithMax = collections.namedtuple('ElementWithMax', ('element',
                                                               'max'))

    def __init__(self):
        self._data = []

    def empty(self):
        return len(self._data) == 0

    def max(self):
        if self.empty():
            raise IndexError('max() on empty stack')
        return self._data[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop() on empty stack')
        return self._data.pop().element

    def push(self, x):
        self._data.append(
            self.ElementWithMax(x, x if self.empty() else max(x, self.max())))
