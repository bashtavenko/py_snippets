"""Tests"""

import unittest

import buy_and_sell_once as m


class BuyTestCase(unittest.TestCase):
    """Test."""

    long_message = True

    def testBuySell(self):
        a = [2, 3, 10, 6, 4, 8, 1]
        self.assertEqual(8, m.buy_and_sell_stock_once(a))

        a = [2, 3, 1, 4, 7, 8]
        self.assertEqual(7, m.buy_and_sell_stock_once(a))


if __name__ == "__main__":
    unittest.main()
