import unittest

import bit_permutations as m


class MyTestCase(unittest.TestCase):

    def testGenerate(self):
        # self.assertListEqual(['0', '1'], m.generate(1))
        self.assertListEqual(["00", "10", "01", "11"], m.generate(2))
        # self.assertListEqual(['000', '100', '010', '110',
        #                       '001', '101', '011', '111'], m.generate(3))


if __name__=="__main__":
    unittest.main()
