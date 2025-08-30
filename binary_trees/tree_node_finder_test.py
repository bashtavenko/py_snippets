import unittest

import tree_node_finder as m


class FinderTestCase(unittest.TestCase):

  def setUp(self):
    self.root = m.Node(4, 'A', children = [
        m.Node(7, 'B', children = [m.Node(9, 'C')]),
        m.Node(11, 'D', children = [m.Node(9, 'E')]),
        m.Node(56, 'F'),
        m.Node(65, 'G', children = [
            m.Node(21, 'H'),
            m.Node(33, 'I')])
    ])

  def testFind(self):
    self.assertEqual('H', m.find_node(self.root, 21))
    self.assertEqual('C', m.find_node(self.root, 9))
    self.assertIsNone(m.find_node(self.root, 42))

if __name__ == '__main__':
  unittest.main()
