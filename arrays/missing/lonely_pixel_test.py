import unittest

import lonely_pixel as m


class LonelyPixelTestCase(unittest.TestCase):
    long_message = True

    def setUp(self):
        self.funcs = [m.lonely_pixel, m.lonely_pixel_with_count]

    def testLonelyPixel(self):
        for f in self.funcs:
            result = f(
                    ([1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 1, 1]))
            self.assertListEqual([(0, 0), (1, 1)], result)


if __name__ == '__main__':
    unittest.main()
