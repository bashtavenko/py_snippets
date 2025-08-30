"""Tests for broken tree."""
import unittest

import broken_tree as m
import bootcamp as bc

class BrokenTreeTestCase(unittest.TestCase):

    def testTraversal(self):
      """Setup a broken tree

                  a
               b     e
            c     d
      """
      d = bc.BinaryTreeNode(data='d')
      b = bc.BinaryTreeNode(data='b',
                           left = bc.BinaryTreeNode(data='c'),
                           right= d)
      # e => d breaks tree property
      e = bc.BinaryTreeNode(data='e', left=d)
      a = bc.BinaryTreeNode(data='a', left=b, right=e)

      m.find_broken_edge(a)

    def studentSearch(self):
      students = [
          Student('m', 2.3),
          Student('k', 2.6),
          Student('a', 3.1),
          Student('b', 3.5),
          Student('f', 3.9)]
      result = bc.search_student(students, 3.0)



if __name__ == '__main__':
    unittest.main()
