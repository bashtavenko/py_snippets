""" 6.13 Rabin-Karp - modular hashing fingerprint search.

Computes hash function for the pattern and then looks for a match by using
the same hash function for each possible substring in the text by moving
left to right. The point is that incrementally updates the text hash as it
moves left to right as opposed to recomputing it all from scratch which is
why it runs in linear time.
"""
import functools


def rabin_karp(t, s):
    """Finds the first occurrence of a substring

    Args:
        t: text to search
        s: substring
    Returns:
        Index of the first occurrence of the substring or -1 if not found
    """
    if len(s) > len(t):
        return -1

    BASE = 26
    # Hashcodes for the substrings of t and s
    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE**max(len(s) - 1, 0) # BASE ^\s-1\

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s) # Found a match

        # Uses rolling has to compute the hash code
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

    # Tries to match s and t[-len(s):]
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)

    return -1