"""Strings bootcamp. """


def is_palindromic(s):
    # ~i == - i - 1
    # all is function that takes generator expression() and returns
    # True if all ll elements are true
    return all(s[i]==s[~i] for i in range(len(s) // 2))


def basic_looping_over_string_digit(s):
    for c in s:
        print(c)
