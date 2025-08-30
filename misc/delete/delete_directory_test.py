"""Tests for delete_directory."""
import unittest

from fs import FileSystem
from fs import Item
from fs import FILE
from fs import FOLDER
import delete_directory as m


class DeleteDirectoryTest(unittest.TestCase):

    def test_delete_basic(self):
      f = FileSystem()
      folder_1 = Item('f1', FOLDER)
      folder_2 = Item('f2', FOLDER)
      f.add(folder_1, Item('i1', FILE))
      f.add(folder_1, Item('i2', FILE))
      f.add(folder_1, folder_2)
      f.add(folder_2, Item('i21', FILE))
      f.add(folder_2, Item('i22', FILE))
      f.add(folder_2, Item('i23', FILE))

      m.delete_tree(f, 'f1')
      # m.delete_my(f, 'f1')

      self.assertTrue(f.is_empty())


if __name__ == '__main__':
    unittest.main()
