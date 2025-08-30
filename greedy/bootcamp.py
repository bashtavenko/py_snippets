"""Greedy bootcamp.
Makes myopic decisions hoping for the best. Never changes decisions.
"""


def change_making(cents):
    # This won't work for coins of
    # [4, 3, 1] if we need to make 6 because greedy would pick up 4, 1, 1
    # but optimum is 3, 3
    COINS = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in COINS:
        # TODO: this loops even after cents == 0
        num_coins += cents // coin
        cents %= coin  # mod cents = cents % coin
    return num_coins


def has_two_sum(a, t):
    """Check if sorted array has two entries that add up to a given value.

    (-2, 1, 2, 4, 7, 11)
    There are entries adding up to 5, 6, 0 and 13 but no 25.  Since array is
    sorted, move from both ends.

    Alternative - binary search
    """
    i, j = 0, len(a) - 1

    while i <= j:
        if a[i] + a[j]==t:
            return True
        elif a[i] + a[j] < t:  # Add some more, assuming sorted ascending
            i += 1
        else:  # a[i] + a[j] > t  # Overshoot, decrease.
            j -= 1
    return False
