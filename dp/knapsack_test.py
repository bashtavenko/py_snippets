"""Tests for knapsack."""
import unittest

import knapsack as m


class KnapsackTestCase(unittest.TestCase):

  def testSuperSimple(self):
      stuff = [
            m.Item(60, 1),
            m.Item(100, 2),
            m.Item(120, 3)
      ]
      self.assertEqual(220, m.optimum_subject_to_capacity(stuff, 5))

  def testSuperSimple2(self):
      stuff = [
          m.Item(10, 4),
          m.Item(4, 2),
          m.Item(7, 3)
      ]
      self.assertEqual(11, m.optimum_subject_to_capacity(stuff, 5))


  def testSimple(self):
      stuff = [
          m.Item(60, 5),
          m.Item(50, 3),
          m.Item(70, 4),
          m.Item(30, 2)
      ]
      self.assertEqual(80, m.optimum_subject_to_capacity(stuff, 5))

  def testMoreComplicated(self):
    stuff = [
            m.Item(65, 20),
            m.Item(35, 8),
            m.Item(245, 60),
            m.Item(195, 55),
            m.Item(65, 40),
            m.Item(150, 70),
            m.Item(275, 85),
            m.Item(155, 25),
            m.Item(120, 30),
            m.Item(320, 65),
            m.Item(75, 75),
            m.Item(40, 10),
            m.Item(200, 95),
            m.Item(100, 50),
            m.Item(220, 40),
            m.Item(99, 10)
    ]
    self.assertEqual(695, m.optimum_subject_to_capacity(stuff, 130))


if __name__ == '__main__':
  unittest.main()
