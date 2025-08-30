"""Tests for most common friends."""
import unittest

import most_common_friends as m

class NetworkTestCase2(unittest.TestCase):
  def setUp(self):
    self.network = m.Network()

  def testBasic(self):
    self.network.add_user(1, 8)
    self.network.add_user(1, 2)
    self.network.add_user(1, 3)

    self.network.add_user(8, 7)

    self.network.add_user(4, 2)
    self.network.add_user(4, 3)
    self.network.add_user(4, 5)

    self.assertEqual(4, self.network.find_user(1))

class Network2TestCase(unittest.TestCase):
  def setUp(self):
    self.network = m.Network2()

  def testBasic(self):
    self.network.add_person(m.Person(1, [8, 2, 3]))
    self.network.add_person(m.Person(8, [7]))
    self.network.add_person(m.Person(2, [4]))
    self.network.add_person(m.Person(3, [4]))
    self.network.add_person(m.Person(4, [5]))

    self.assertEqual(4, self.network.find_user(1))



if __name__ == '__main__':
  unittest.main()
