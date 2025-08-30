"""Offline sample."""

import random


def make_sample(k, a):
    for i in range(k):
        r = random.randint(i, len(a) - 1)
        a[i], a[r] = a[r], a[i]
