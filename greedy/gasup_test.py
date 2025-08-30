import unittest

import gasup


class MyTestCase(unittest.TestCase):

    def test_ample(self):
        result = gasup.find_ample_city(
            [50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100]
        )
        self.assertEquals(3, result)  # City D


if __name__=="__main__":
    unittest.main()
