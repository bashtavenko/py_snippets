import unittest

import equilibrium as m


class EquilibriumTestCase(unittest.TestCase):

    def setUp(self):
        self.funcs = [m.find_bf, m.find_bf2, m.find_on]

    def testFind(self):
        for f in self.funcs:
            self.assertEqual(2, f([2, 1, 4, 3]))
            self.assertEqual(1, f([-1, 3, 2, -3]))
            self.assertEqual(0, f([5, -1, 1]))
            self.assertEqual(0, f([5]))


if __name__ == "__main__":
    unittest.main()
