"""Primitive types bootcamp."""

# ^ = XOR. 0^0 = 0; 0^1 = 1
# XOR of two bits is equivalent to mod 2


def count_ones(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def count_ones_plus(x):
    """Brian Kernighan algo.
    This is efficient because it loops only ones
    """
    num_bits = 0
    while x:
        # Turn off rightmost bit.
        # Not the least significant one and therefore x
        # decreases faster.
        # 13 = 13 - 12 - 8 - 0
        x &= x - 1  # x = x & (x - 1)
        num_bits += 1
    return num_bits


def set_bit(x, n):
    return x | 1 << n


def reset_bit(x, n):
    # Set up a mask, example 1101
    # ~ (compliment) flips the bits
    # ~2 = -3, i.e. 0010 => 1101 where "1" is minus
    return x & ~(1 << n)


def test_bit(x, n):
    return (x & (1 << n)) > 0


def toggle(x, n):
    # ^ is XOR 8 ^ 3 = 11
    return x ^ (1 << n)


def turn_off_right_most_one(x):
    # x      (6)  110
    # x - 1  (5)  101
    # x & (x-1)   100
    # NOT the least significant one
    # Erase lowest bit set
    return x & (x - 1)


def get_digits_of_number(x, d):
    """Returns digit of the number at the given position.

    Args:
        x: number
        d: digit position, LSD is 0

    For example:
     Number = 329 which is 3 * 10^2 + 2 * 10^1 + 9 * 10^0
     Therefore, to get digit we are doing reverse:
     For n = 1
     329 // 10 => 32
     32 % 10 => 2
     (329, 0) = > 9
    """
    return (x // (10**d)) % 10
