"""10.4 Returns the largest integer whose square is less than or equal the given number.

Input: 16 => 4
300 => 17 since 17 ^ 2 = 289 and 18 ^2 =  324
21 => 4
25 => 5
"""


def square_root(k):
    # Since numbers are increasing, it's just like sorted array
    lo, hi = 0, k
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        mid_square = mid * mid  # Here's the trick
        if k < mid_square:  # mid_square is too high
            hi = mid - 1
        else:
            lo = mid + 1

    return lo - 1


if __name__=="__main__":
    print(square_root(5))
