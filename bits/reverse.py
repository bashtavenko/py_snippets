"""4.8 Digits and bits reversals."""

"""
Mod 10 division to reverse
1132 => 2311
1132 % 10 = 2   0 * 10 + 2 = 2
113 % 10 = 3    2 * 10 + 3 = 23
11 % 10 = 1     23 * 10 + 1 = 231
1 % 10 = 1      231 * 10 + 1 = 2311
"""


def reverse_digits(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        # result * 10 meaning "shift" left on every loop
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


def reverse_digits_bf(x):
    chars = list(str(x))
    for i in range(len(chars) // 2):  # Only need up to half-way
        chars[i], chars[~i] = (
            chars[~i],
            chars[i],
        )  # ~2 == -3 and a[~1] = second from the right

    result_str = "".join(chars)
    return int(result_str)
