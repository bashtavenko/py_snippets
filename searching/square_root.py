"""11.5 Real square root.


"""
import math


def square_root(x):
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not math.isclose(left, right):  # requires > 2.7
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if x < mid_squared:
            right = mid
        else:
            left = mid

    return left


if __name__ == '__main__':
    print (square_root(2))