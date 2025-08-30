"""Tests for histogram bootcamp."""
import unittest

import fs as m


class FsTestCase(unittest.TestCase):

    def test_match_oneLevel(self):
      fs = m.FileSystem()
      folder_1 = m.Item('f1', m.FOLDER)
      fs.add(folder_1, m.Item('i1', m.FILE))
      fs.add(folder_1, m.Item('i2', m.FILE))

      result = fs.match('f1')
      self.assertEqual(2, len(result))

    def test_match_multiLevels(self):
        fs = m.FileSystem()
        folder_1 = m.Item('f1', m.FOLDER)
        folder_2 = m.Item('f2', m.FOLDER)
        fs.add(folder_1, m.Item('i11', m.FILE))
        fs.add(folder_1, folder_2)
        fs.add(folder_2, m.Item('i21', m.FILE))
        self.assertIsNotNone(fs.match('i21'))

    def test_delete(self):
        fs = m.FileSystem()
        folder_1 = m.Item('f1', m.FOLDER)
        fs.add(folder_1, m.Item('i1', m.FILE))
        fs.add(folder_1, m.Item('i2', m.FILE))

        fs.delete('i1')
        self.assertEqual(0, len(fs.match('i1')))

    def test_isDirectory(self):
        fs = m.FileSystem()
        folder_1 = m.Item('f1', m.FOLDER)
        fs.add(folder_1, m.Item('i1', m.FILE))
        fs.add(folder_1, m.Item('i2', m.FILE))
        self.assertTrue(fs.is_directory('f1'))
        self.assertFalse(fs.is_directory('i1'))
        self.assertFalse(fs.is_directory('i10'))

    def test_isEmpty(self):
        fs = m.FileSystem()
        folder_1 = m.Item('f1', m.FOLDER)
        fs.add(folder_1, m.Item('i1', m.FILE))
        fs.add(folder_1, m.Item('i2', m.FILE))

        fs.delete('i1')
        fs.delete('i2')
        fs.delete('f1')
        self.assertTrue(fs.is_empty())

    def test_delete_nonEmpty(self):
        fs = m.FileSystem()
        folder_1 = m.Item('f1', m.FOLDER)
        fs.add(folder_1, m.Item('i1', m.FILE))
        fs.add(folder_1, m.Item('i2', m.FILE))

        with self.assertRaises(ValueError):
            fs.delete('f1')


if __name__ == '__main__':
    unittest.main()
