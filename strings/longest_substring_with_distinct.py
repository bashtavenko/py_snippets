"""Given a string, find the longest substring with k distinct characters.

This is similar to longest_subarray.py

"""

import collections


def find_longest(s, n):
    current, longest = "", ""

    for i, c in enumerate(s):
        current = append_character(current, c, n)
        longest = current if len(current) > len(longest) else longest
    return longest


def append_character(substring, c, n):
    substring += c

    unique = collections.defaultdict(set)
    unique_start = 0
    for i, c in enumerate(reversed(substring)):
        unique[c] = 1

        if len(unique) > n:
            unique_start = len(substring) - i
            break

    return substring[unique_start:]


def find_longest_2(s):
    char_count = {}
    window = []
    for i in range(1, len(s)):
        if s[i]==s[i - 1]:
            window.append(s[i])
        elif len(window) > 0:
            window.append(window[-1])
            key = window[0]
            char_count[key] = max(char_count.get(key, 0), len(window))
            window = []

    return char_count
