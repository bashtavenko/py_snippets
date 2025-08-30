"""Buy and sell stock once.

Simultaneous min and max:
1. Conventional: n - 1 comparisons x 2 = 2n - 2
2. Better: compare pairs. Compare input with each other and
then compare smallest with current min and largest with
current max. 3 [n/2]
"""
import sys


def buy_and_sell_stock_once(prices):
    # That's the trick - min_price = sys.maxint
    # max_profit = 0
    min_price_so_far, max_profit = sys.maxint, 0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit
