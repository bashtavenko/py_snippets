import unittest

import replace_and_remove as m


class MyTestCase(unittest.TestCase):
    def test_works(self):
        s = list("acdbbca")
        m.replace_and_remove(s)
        self.assertEqual(list("ddcdcdd"), s)


if __name__ == "__main__":
    unittest.main()
