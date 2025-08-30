"""Tests for LRU cache."""
import unittest

import lru_cache as m


class LruCacheTestCase(unittest.TestCase):

  def testCache(self):
    cache = m.LRUCache(2)
    cache.insert('a', 1)
    cache.insert('b', 2)
    cache.insert('c', 3) # This should evict 'a', leaving us with 'b' and 'c'

    self.assertTupleEqual((False, None), cache.lookup('a'))

    cache.insert('d', 4) # This should evict 'b'
    self.assertTupleEqual((False, None), cache.lookup('b'))

  def testCache_read(self):
    cache = m.LRUCache(2)
    cache.insert('a', 1)
    cache.insert('b', 2)
    result = cache.lookup('a')
    cache.insert('c', 3) # This should evict 'b', leaving us with 'a' and 'c'

    self.assertTupleEqual((False, None), cache.lookup('b'))


if __name__ == '__main__':
    unittest.main()
