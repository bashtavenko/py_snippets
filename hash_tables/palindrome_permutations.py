"""12.1 Test for palindrome permutations.

Palindrome reads the same from both ends 'level', 'rotator'.

Check if characters of string can be permuted to form a palindrome.

'edified' -> 'deified' permuted and now it is palindrome

What number of character counts are needed for palindrome?
'aba' a:2 b:1  odd
'abcba' a:2, b:2, c:1 odd
'abccba' a:2, b:2, c:2 even
'aabbcbbaa' a: 4, b: 4, c: 1 odd
"""

import collections


def can_be_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == "__main__":
    print(can_be_palindrome("edified"))
    print(can_be_palindrome("abc"))
