import unittest

import score_combinations as m

class MyTestCase(unittest.TestCase):

    def testScores(self):
       # self.assertEquals(4, m.num_combinations(12, [2, 3, 7]))
       self.assertEquals(2, m.num_combinations(7, [2, 3, 7]))

if __name__ == '__main__':
    unittest.main()
