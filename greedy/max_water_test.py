import unittest

import max_water


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            48,
            max_water.get_max_water(
                [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
            ),
        )


if __name__=="__main__":
    unittest.main()
