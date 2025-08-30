""" LRU cache.

OrderedDict keeps the order, but we need to re-add element
on lookup and insert.

We change order elements on lookup and on insert
delete the extra one.
"""

import collections


class LRUCache:

    def __init__(self, capacity):
        # It remembers the order of elements and behaves like a regular dict
        self.table = collections.OrderedDict()
        self.capacity = capacity

    def lookup(self, key):
        if key not in self.table:
            return False, None

        # Have key. Re-add it on lookup, that's the trick.
        # if it was [a, b] and we looked up 'b', it will be [b, a]
        value = self.table.pop(key)
        self.table[key] = value  # Stack, essentially
        return True, value

    def insert(self, key, value):
        if key in self.table:
            value = self.table.pop(key)  # We may exceed capacity
        elif self.capacity <= len(self.table):  # Check capacity before adding
            self.table.popitem(last=False)  # First one is gone
        self.table[key] = value  # Finally add

    def erase(self, key):
        return self.table.pop(key, None) is not None
