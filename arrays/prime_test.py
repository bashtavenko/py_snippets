import unittest

import prime


class PrimeTestCase(unittest.TestCase):
    def setUp(self):
       #self.func = prime.generate_primes_bf
       self.func = prime.generate_primes

    def testPrimes(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17], self.func(18))


if __name__ == '__main__':
    unittest.main()
