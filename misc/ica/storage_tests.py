import misc.ica.storage as storage
import unittest

class StorageTests(unittest.TestCase):
    def setUp(self):
        self.storage = storage.Storage()

    def test_query(self):
        self.storage.add_file("file.txt", 5)
        self.storage.add_file("/dir/file.txt", 10)
        self.storage.add_file("/dir/dir/file.txt", 15)
        result = self.storage.query("dir", "file.txt")
        expected = ["/dir/dir/file.txt(15)", "/dir/file.txt(10)" ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
