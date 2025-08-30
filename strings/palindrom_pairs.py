"""Palindrome pairs.

Given an array of strings with differences in size at most 1, find the number of pairs of strings
which when concatenated become a palindrome.

['ab', 'abc', 'ba', 'feg']
abba
baab
abcba
"""


def count_palindrom_pairs(a):
    def is_palindrome(s):
        for i in range(len(s) // 2):
            if s[i]!=s[~i]:
                return False
        return True

    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                word = a[i] + a[j]
                # .. or simply
                # if word == word[::-1]:
                if is_palindrome(word):
                    count += 1
                    print(a[i] + a[j])
    return count


def count_palindrom_pairs_better(a):
    """Better counting.

    What makes a string palindrome? If it reads the same from both ends which
    means we could divide string by half, reverse one half and check with the
    first one. abba => ab, ba => ab, ab == palindrome. If two equal length
    strings are given in two separate arrays, we check every string with
    reversed version. If strings differs by at most 1, we need to use the
    length of a shortest string: ab, cba => abcba, for string 'ab' => 'cba'.

    In order to find palindrome we can look for reversed pair in the array.
    For example, if all strings were the same length and given ['aw', 'ze',
    'dc', 'wa', 'ez'], we can reverse 'aw' => 'wa' and check to see if 'wa' is
    in the list.  For the strings that are longer, we can simply ignore the
    extra character, meaning given 'abc' we only need to check for 'ba' par in
    order to form 'abcba'.

    So essentially, 1. Find minimum length; 2. Loop through and make reversed
    words from min number of characters, there can be multiple, so for key =>
    it should be list; 3. Make candiate word and check it.
    """
