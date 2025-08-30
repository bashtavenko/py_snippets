"""Tests for shortest subarray."""
import unittest

import shortest_subarray as m

class ShortestSubarrayTestCase(unittest.TestCase):

  def testSubarray(self):
    paragraph = ['apple', 'banana', 'apple', 'apple', 'dog',
                 'cat', 'apple', 'dog', 'banana', 'apple',
                 'cat', 'dog']
    keywords = ['banana', 'cat']
    result = m.find_smallest_subarray_covering_set(paragraph, keywords)
    self.assertTupleEqual((8, 10), result)

if __name__ == '__main__':
    unittest.main()
