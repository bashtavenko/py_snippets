"""6.1 Interconnect strings and ints."""

import functools
import string


def int_to_string(x):
    is_negative = False

    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord("0") + x % 10))
        x //= 10
        if x == 0:
            break

    return ("-" if is_negative else "") + "".join(reversed(s))


def string_to_int(s):
    # reduce https://realpython.com/python-reduce-function/
    return functools.reduce(
        lambda x, y: x * 10 + string.digits.index(y),
        # Iterable
        #  Chops off the first character if minus
        # Filter list with boolean
        s[s[0] == "-" :],
        0,  # Initializer
        0,  # Initializer
    )
    # This never worked
    # * (-1 if s[0] == "-" else 1)
