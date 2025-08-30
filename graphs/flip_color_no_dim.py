"""Variation of Flip Color problem with unknown matrix dimension.

Its just a matter of running DFS, but since matrix is unknown, DFS needs to
make calls to an external interface.

Some key points:
Represent directions with NORTH, EAST, SOUTH, WEST = range(4). In that way
a direction change could be translated to commands given current direction:
NORTH -> EAST: right
EAST -> WEST: right, right

Position is stored relative to the starting point in defaultdict of set where
key is X and values are Y's of it:
 {0: {0}}, moved EAST, {0: {0}, 1: {0}}
 {0: {0}}, moved SOUTH, {0: {0, 1}}
Every move updates current position. Checking for visited is just matter of
looking up a key in defaultdict.

This requires more work, but that's the idea.
"""

import collections

NORTH, EAST, SOUTH, WEST = range(4)
OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

Position = collections.namedtuple('Position', ('x', 'y'))

class ColorFlipper:
  def __init__(self, runner):
    self.position = Position(0, 0)
    self.direction = int(NORTH)
    self.runner = runner
    self.visited = collections.defaultdict(set)

  def flip_color(self):
    self._run_dfs()

  def _run_dfs(self):
    """That's the gist of it."""
    self._flip_and_mark_visited()
    for direction in NORTH, EAST, SOUTH, WEST:
      moved = self._try_to_run(direction)
      if moved and not self._is_visited():
        self.run_dfs()

  def _try_to_run(self, direction):
    """Try to run in a given direction."""
    diff = abs(direction - self.direction)
    # Make a turn.
    if diff == 3:
      self.runner.turn_left(1)
    else:
      self.runner.turn_right(diff)
    self.direction = direction
    # Now try to move in that direction.
    moved = self.runner.try_to_run()
    if moved:
      offset = OFFSETS[direction]
      self.position = Position(self.position.x + offset[0],
                               self.position.y + offset[1])
    return moved

  def _flip_and_mark_visited(self):
    self.runner.flip_color()
    self.visited[self.position.x].add(self.position.y)

  def _is_visited(self):
    return (self.position.x in self.visited and
        self.position.y in self.visited[self.position.x])

class Runner:
  def flip_color(self):
    """Flips current cell color."""

  def try_to_run(self):
    """Advances one white cell in the given direction.

    Returns False if the next cell is black or out of bound.
    """

  def turn_left(self, n):
    """Turns left n times but do not move."""

  def turn_right(self, n):
    """Turns right n times but do not move."""
