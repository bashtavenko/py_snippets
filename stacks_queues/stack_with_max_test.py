"""Tests for stack with max."""
import unittest

import stack_with_max as m

class StackTestCase(unittest.TestCase):
    def testStack(self):
      stack = m.Stack()
      stack.push(2)
      stack.push(10)
      stack.push(7)

      self.assertEqual(10, stack.max())
      self.assertEqual(7, stack.pop())
      self.assertEqual(10, stack.pop())
      self.assertEqual(2, stack.max())
      self.assertEqual(2, stack.pop())
      self.assertTrue(stack.empty())


if __name__ == '__main__':
    unittest.main()
