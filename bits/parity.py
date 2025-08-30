"""Parity.
4.1 Compute parity

If numbers of ones is odd, return 1, otherwise return 0
1011 => 1
10001000 = > 0
"""


def brute_force(x):
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result % 2


def brute_force_41(x):
    result = 0
    while x:
        # XOR of two bits == mod 2, no need for % at end
        result ^= x & 1
        x >>= 1
    return result


def parity(x):
    result = 0
    while x:
        # x &(x - 1) equals x with the lowest(rightmost) set bit erased
        x &= x - 1  # Turns of rightmost
        result ^= 1  # Flips the lowest because we only care about 1 or 0
    return result
