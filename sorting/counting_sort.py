"""Counting and radix sorts.

Idea of the counting sort - determine for each input element x, the number of elements less
than x. If we know that, we know where to put this element in the sorted output.
For example, if 17 elements less than x, then x belongs to in position 18.

In order for this work the sort must be stable, that is if objects with EQUAL KEYS appear
in the same order in sorted output as there are in input:

If sorting by first letter with stable sort
peach
straw
apple
spork

apple
peach
straw  # straw is BEFORE spork because this is how they are in the input
spork
"""
import collections


def counting_sort_classic(a, r):
    """Classical counting sort per CRLS.

    Args:
      a: Iterable of integer elements
      r: Possible number of values

    Returns:
      Sorted list
    """
    c = [0] * r # Counter list, c[0] - number of 0s, up to number of digits
    b = [0] * len(a) # Result, same size as input

    # Count how many elements are in the input
    # For [2, 5, 3, 0, 2, 3, 0, 3] it will be
    #     [2, 0, 2, 3, 0, 1]  (two 2s, three 3s, zero 4s, etc)
    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1

    # How many elements less than or equal to i digit?
    #  For [2, 0, 2, 3, 0, 1] it is
    #      [2, 2, 4, 7, 7, 8]
    # Two elements less than or equal 1 (0, 0)
    # Four elements less than or equal 2 (0, 0, 2, 2)
    # Seven elements less than or equal 3 (0, 0, 2, 2, 3, 3, 3)
    for i in range(1, r): # going by k, nothing is less than zero
        c[i] = c[i] + c[i - 1]

    # Put elements in correct place
    for j in range(len(a) - 1, -1, -1): # Right to left accounts for duplicates
        b[c[a[j]] - 1] = a[j]
        c[a[j]] = c[a[j]] - 1 # Placed one element, drop the counter

    return b


def counting_sort(a, r):
    """More Pythonic version of counting sort.

    Args:
      a: Iterable of integer elements
      r: Possible number of values

    Returns:
      Sorted list
    """
    b = collections.defaultdict(int)

    # 1. Count
    c = collections.Counter(a)

    # 2. Rollup counters (how many numbers are less than then a given one)
    for i in range(1, r):
        c[i] = c[i] + c[i - 1]

    # 3. Put digits in correct position
    for j in reversed(range(len(a))):
        digit = a[j]
        b[c[digit] - 1] = digit
        c[digit] -= 1

    return b.values()


def counting_sort_on_digit(a, d, r):
    """
    Counting sort for one digit of the number

    Args:
      a: Iterable of integer numbers
      d: Digit index with 0 being LSD
      r: Possible number of values. It is 10 for decimal numbers

    Returns:
      Sorted list
    """
    def get_digit_of_number(n, d):
        """Returns digit of the number at given index.

        329 = 3*10^2 + 2*10^1 + 9*10**0
        Therefore, getting a digit is reverse of that.
        """
        return n // 10 ** d % 10

    b = collections.defaultdict(int)
    c = collections.Counter([get_digit_of_number(x, d) for x in a])

    for i in range(1, r):
        c[i] = c[i] + c[i - 1]

    for j in reversed(range(len(a))):
        # These two lines are the only difference between regular counting sort
        entry = a[j]  # That's the whole number
        digit = get_digit_of_number(entry, d) # Digit of that number at index
        b[c[digit] - 1] = entry
        c[digit] -= 1

    return b.values()


def radix_sort(a, d, r):
    """
    Radix sort of the number

    Args:
      a: Iterable of integer numbers
      d: Digit index with 0 being LSD
      r: Possible number of values. It is 10 for decimal numbers

    Returns:
      Sorted list
    """
    for i in range(d):
        a = counting_sort_on_digit(a, i, r)

    return a
