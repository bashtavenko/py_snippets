"""Tests for flip color."""
import unittest

import collections
import flip_color_no_dim as m

class FlipColorTestCase(unittest.TestCase):

  def setUp(self):
    self.matrix = [[1, 0, 1],
                   [1, 0, 1],
                   [0, 0, 1]]
    self.runner = Runner(m.Position(0, 1), self.matrix)
    self.flipper = m.ColorFlipper(self.runner)

  def testFlipAndMark(self):
    self.flipper._flip_and_mark_visited()
    self.assertEqual(1, self.matrix[0][1])
    self.assertTrue(self.flipper._is_visited())

  def testTryToRun(self):
    moved = self.flipper._try_to_run(m.SOUTH)
    self.assertTrue(moved)


class Runner:
  def __init__(self, absolute_position, matrix):
    self.matrix = matrix
    self.position = m.Position(0, 0)
    self.direction = int(m.NORTH)
    self.absolute_position = absolute_position

  def flip_color(self):
    """Flips current cell color."""
    pos = self._get_absolute_position(self.position)
    self.matrix[pos.x][pos.y] = 1 - self.matrix[pos.x][pos.y]

  def try_to_run(self):
    """Advances one white cell in the given direction.

    Returns False if the next cell is black or out of bound.
    """
    import pdb; pdb.set_trace()
    offset = m.OFFSETS[self.direction]
    new_relative_position = m.Position(
        self.position.x + offset[0],
        self.position.y + offset[1])
    pos = self._get_absolute_position(new_relative_position)
    return (0 < pos.x < len(self.matrix) and
            0 < pos.y < len(self.matrix[0]) and
            self.matrix[pox.x][pos.y] == 0)

  def turn_left(self, n):
    """Turns left n times but do not move."""
    self.direction = abs(self.direction - n) % 4

  def turn_right(self, n):
    """Turns right n times but do not move."""
    self.direction = (self.direction + n) % 4

  def _get_absolute_position(self, position):
    return m.Position(self.absolute_position.x + position.x,
                      self.absolute_position.y + position.y)


if __name__ == '__main__':
  unittest.main()
