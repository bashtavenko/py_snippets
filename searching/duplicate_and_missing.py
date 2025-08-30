"""11.10 Find duplicate and missing numbers.

Array has n-elements, but we have n-1
(n - 1) * n * 0.5

Array contains n - 1 integers
n = 6, but we have 5 => [5, 3, 0, 1, 2]
((n - 1)) * n / 2 => 5 * 6 / 2 = 15
sum = 11 (5 + 3 + 0 + 1 + 2)
15 - 11 = 4 (missing 4)

1. Sum.  Sum of all numbers in the 0 - (n - 1) array is ((n-1) * n) / 2,
subtract from this number sum of all numbers. 

If exactly one element appears twice, the result will be sum - (n-1)n / 2
Array contains n + 1 integers (one extra)
n:5  3, 3, 0, 1, 2, 4
sum: 13
4 * 5 / 2: 10
13 - 10 = 3

2. XOR

3. Hash table
"""


def find_duplicate_and_missing(a):
    """Find missing and repeating element.

    Array of n length that contains 0 - n-1.
    Initially all elements were unique, one element was changed to another.
    n:6 3, 2, 2, 1, 4, 5
    Answer: 0 - missing, 2 - duplicate
    """
