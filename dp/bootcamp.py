""" Dynamic Programming bootcamp.

Just like D/C breaks into subproblems, but subproblems overlap. Subproblems share
 subproblems which is why they need to be cached.

DP is for optimization problems.



"""
import itertools


def fibo(n):
    """0 1 1 2 3 5 8 13"""
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def fibo_cached(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibo_cached(n - 1) + fibo_cached(n - 2)
    return cache[n]


def fibo_iterative(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


def find_maximum_subarray(a):
    # This is similar to buy-sell stock once
    # There is also a D&C solution
    """
      for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
      return max_profit
    """
    min_sum = max_sum = 0
    # itertools.accumulate: 1,2,3,4,5 --> 1 3 6 10 15
    for running_sum in itertools.accumulate(a):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum
