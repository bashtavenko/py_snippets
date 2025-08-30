"""16.9 Pickup coins for max gain.

Even number of coins, each player can take at the ends.

25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 1, 25 5, 10

C = array, C[2] = 10
R(a, b) = max revenue. 'a' and 'b' are indexes of the remaining coins (ends).

If first player selects coin at 'a' and  the second player pays optimally
first player revenue:
  C[a] + S(a + 1, b) - R(a+1, b)
where S is the sum of the coins from positions a to b. If he selects 'b'
  C[b] + S(a, b - 1) - R(a, b - 1)

Since first player wants to maximize his revenue, he chooses the greater of
the two.

A better strategy could be to minimize another player revenue, i.e. max-min
"""
